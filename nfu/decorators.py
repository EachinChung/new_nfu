from functools import wraps

from flask import request, jsonify

from nfu.models import User
from nfu.token import validate_token


def check_access_token(func):
    """
    检查用户的access_token是否合法
    因为有账号才能拿到token，故不考虑，账号不存在的情况

    :param func: 使用此装饰器的函数
    :return: 指向新函数，或者返回错误
    """

    @wraps(func)
    def wrapper(*args, **kw):
        token = request.form.get('access_token')
        validate = validate_token(token)

        # 验证 token 是否通过
        if validate[0]:
            user = User.query.get(validate[1]['id'])

        else:
            return jsonify({'message': validate[1]})

        return func(user, *args, **kw)

    return wrapper
