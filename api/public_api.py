import json
import security.jwtSecurity
from flask import Blueprint, request

public_api = Blueprint('public_api', __name__)


@public_api.route("/search", methods=['GET'])
@security.jwtSecurity.requires_auth
def search():
    """

    :return:
    """
    pass


@public_api.route("/read", methods=['GET'])
@security.jwtSecurity.requires_auth
def read():
    """

    :return:
    """
    pass


@public_api.route("/createUser", methods=['POST'])
def createUser():
    pass
