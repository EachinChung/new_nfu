from json import loads

from flask import Blueprint, jsonify, g, request

from nfu.extensions import db
from nfu.common import check_access_token
from nfu.models import Dormitory

user_bp = Blueprint('user', __name__)


@user_bp.route('/get')
@check_access_token
def get_user():
    """
    获取用户数据
    :return:
    """
    dormitory = Dormitory.query.get(g.user.room_id)
    return jsonify({
        'id': g.user.id,
        'name': g.user.name,
        'email': g.user.email,
        'dormitory': dormitory.building + ' ' + dormitory.floor + ' ' + str(dormitory.room)
    })


@user_bp.route('/dormitory/update', methods=['POST'])
@check_access_token
def update_dormitory():
    """
    更新宿舍信息
    :return:
    """
    data = loads(request.get_data().decode("utf-8"))
    room_id = int(data['room_id'])
    g.user.room_id = room_id
    db.session.add(g.user)
    db.session.commit()

    return jsonify({'adopt': True, 'message': 'success'})