import json
import security.jwtSecurity

from flask import Blueprint, request
from services.database.DBConn import bucket

secure_api = Blueprint('secure_api', __name__)


# @secure_api.route("/add", methods=['POST'])
# # @security.jwtSecurity.requires_auth
# def add_books():
#     # http://127.0.0.1:5000/secure/add?book_name=README.txt
#     """
#     param: book_name
#     :return: 'success' or 'error'
#     """
#     book_name = file = request.files['book_name']
#     upload_book(book_name)
#     return json.dumps({'success': True})


def upload_book(file_name):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(file_name)
    with open(file_name, 'rb') as my_file:
        blob.upload_from_file(my_file)

#########################################################

# @secure_api.route("/update", methods=['PUT'])
# @security.jwtSecurity.requires_auth
# def update_books():
#     # http://127.0.0.1:5000/secure/add
#     """
#     param: book_name
#     :return: 'success' or 'error'
#     """
#     book_name = request.args.get("book_name")
#     upload_book(book_name)
#     return json.dumps({'success': True})
#
#
# @secure_api.route("/delete", methods=['DELETE'])
# @security.jwtSecurity.requires_auth
# def delete_books():
#     # http://127.0.0.1:5000/secure/delete
#     """
#     param: book_name
#     :return: 'success' or 'error'
#     """
#     book_name = request.args.get("book_name")
#     delete_book(book_name)
#     return json.dumps({'success': True})


