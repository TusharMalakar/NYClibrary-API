import json
import security.jwtSecurity
from flask import Blueprint, request

public_api = Blueprint('public_api', __name__)


@public_api.route("/search", methods=['GET'])
@security.jwtSecurity.requires_auth
def search():
    # http://0.0.0.0:5000/public/search
    """

    :return:
    """
    pass


@public_api.route("/read", methods=['GET'])
@security.jwtSecurity.requires_auth
def read():
    # http://0.0.0.0:5000/public/read
    """

    :return:
    """
    pass


@public_api.route("/createUser", methods=['POST'])
def createUser():
    # http://0.0.0.0:5000/public/createUser
    pass
