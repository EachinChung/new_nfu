from os import getenv
from random import randint

from flask import Blueprint, g, jsonify
from redis import Redis
from werkzeug.security import generate_password_hash

from nfu.common import check_access_token, get_token
from nfu.expand.email import send_verification_code
from nfu.expand.token import validate_token
from nfu.extensions import db
from nfu.models import User
from nfu.nfu_error import NFUError

validate_bp = Blueprint('validate', __name__)


@validate_bp.route('/activation')
def activation() -> jsonify:
    """
    验证邮箱合法性，并激活账号
    因为有账号才能拿到token，故不考虑，账号不存在的情况
    :return: json
    """
    try:
        validate = validate_token(get_token(), 'EMAIL_TOKEN')
    except NFUError as err:
        return jsonify({'code': err.code, 'message': err.message})

    # 验证账号是否激活
    user = User.query.get(validate['id'])
    if user is not None:
        return jsonify({'code': '2000', 'message': '该账号已激活'})

    r = Redis(host='localhost', password=getenv('REDIS_PASSWORD'), port=6379)

    try:  # 从 Redis 读取注册信息
        name = r.hget(f"sign-up-{validate['id']}", 'name').decode('utf-8')
        password = r.hget(f"sign-up-{validate['id']}", 'password').decode('utf-8')
        room_id = r.hget(f"sign-up-{validate['id']}", 'roomId').decode('utf-8')
        email = r.hget(f"sign-up-{validate['id']}", 'email').decode('utf-8')
    except AttributeError:
        return jsonify({'code': '2000', 'message': '该链接已失效'})

    # 删除缓存中的数据
    r.delete(f"sign-up-{validate['id']}")

    # 把用户数据写入 MySql
    user = User(
        id=validate['id'],
        name=name,
        password=generate_password_hash(password),
        room_id=room_id, email=email, jw_pwd=password
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'code': '1000', 'message': '激活成功'})


@validate_bp.route('/verification-code')
@check_access_token
def get_verification_code() -> jsonify:
    """
    生成六位验证码
    :return:
    """

    code = randint(100000, 999999)

    r = Redis(host='localhost', password=getenv('REDIS_PASSWORD'), port=6379)
    r.set(g.user.id, code, ex=300)

    send_verification_code(g.user.email, g.user.name, code)

    return jsonify({'code': '1000', 'message': '验证码已发送至您的邮箱，请查看'})
