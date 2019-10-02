import json
import security.jwtSecurity
from flask import Blueprint, request

secure_api = Blueprint('secure_api', __name__)


@secure_api.route("/add", methods=['PUT'])
@security.jwtSecurity.requires_auth
def add_books():
    """

    :return:
    """
    pass


@secure_api.route("/delete", methods=['DELETE'])
@security.jwtSecurity.requires_auth
def delete_books():
    """

    :return:
    """
    pass


