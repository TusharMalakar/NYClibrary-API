import json
import security.jwtSecurity
from api.public_api import search_a_book
from flask import Blueprint, request
from services.database.DBConn import bucket

secure_api = Blueprint('secure_api', __name__)


@secure_api.route('/add', methods=['PUT'])
# @security.jwtSecurity.requires_auth
def add_books():
     # http://127.0.0.1:5000/secure/add
     # body ={
     #
     #     key = "book_name" & value = "README.txt"
     #    }
    """
    param: book_name
    :return: 'success' or 'error'
    """
    files = request.files['file']
    file = files.__dict__['filename']
    upload_book(file)
    status = search_a_book(file)
    return status


def upload_book(file_name):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(file_name)
    with open(file_name, 'rb') as my_file:
        blob.upload_from_file(my_file)



@secure_api.route("/delete", methods=['DELETE'])
# @security.jwtSecurity.requires_auth
def delete_books():
    # http://127.0.0.1:5000/secure/delete
    """
    param: book_name
    :return: 'success' or 'error'
    """
    book_name = request.args.get("book_name")
    try:
        delete_blob(book_name)
        return json.dumps({'success': True})
    except Exception as e:
        print(e)
        return json.dumps({"error":"404 not found"})



def delete_blob(blob_name):
    """Deletes a blob from the bucket."""
    blob = bucket.blob(blob_name)
    blob.delete()
    print('Blob {} deleted.'.format(blob_name))
