import json
from flask import Blueprint, request

secure_api = Blueprint('secure_api', __name__)


@secure_api.route("/", methods=['PUT'])
def add_books():
    """

    :return:
    """
    pass


@secure_api.route("/", methods=['DELETE'])
def delete_books():
    """

    :return:
    """
    pass
