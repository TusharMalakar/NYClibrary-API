import json
from flask import Blueprint, request

public_api = Blueprint('public_api', __name__)


@public_api.route("/", methods=['GET'])
def search():
    """

    :return:
    """
    pass


@public_api.route("/", methods=['GET'])
def read():
    """

    :return:
    """
    pass
