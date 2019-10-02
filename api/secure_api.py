import json
import security.jwtSecurity
from flask import Blueprint, request

secure_api = Blueprint('secure_api', __name__)


@secure_api.route("/add", methods=['PUT'])
@security.jwtSecurity.requires_auth
def add_books():
    # http://0.0.0.0:5000/secure/add
    """

    :return:
    """
    pass


@secure_api.route("/delete", methods=['DELETE'])
@security.jwtSecurity.requires_auth
def delete_books():
    # http://0.0.0.0:5000/secure/delete
    """

    :return:
    """
    pass


