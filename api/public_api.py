import json
# import security.jwtSecurity
from flask import Blueprint, request
from services.database.DBConn import bucket

public_api = Blueprint('public_api', __name__)


@public_api.route("/search", methods=['GET'])
def search():
    # http://127.0.0.1:5000/public/search

    return json.dumps({'success': True, 'message': "book is ready to read"})


@public_api.route("/read", methods=['GET'])
def read():
    # http://127.0.0.1:5000/public/read
    """

    :return:
    """
    return json.dumps({'success': True})


@public_api.route("/createUser", methods=['POST'])
def createUser():
    # http://127.0.0.1:5000/public/createUser
    return json.dumps({'success': True})


def download_book(file_name):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(file_name)
    blob.download_to_filename(file_name)


def list_of_books():
    pass


download_book("3.txt")

