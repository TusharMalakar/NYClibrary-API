import json
# import security.jwtSecurity
from flask import Blueprint, request
from services.database.DBConn import (bucket, client, bucket_name)

public_api = Blueprint('public_api', __name__)


@public_api.route("/search", methods=['GET'])
def search():
    # http://127.0.0.1:5000/public/search
    book_name = request.args.get('book_name')
    status = search_a_book(book_name)
    return status


@public_api.route("/createUser", methods=['POST'])
def createUser():
    # http://127.0.0.1:5000/public/createUser
    return json.dumps({'success': True})


def download_book(file_name):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(file_name)
    blob.download_to_filename(file_name)


# @public_api.route("/book_list", methods=['GET'])
def list_of_books():
    """
    :return: iterable_object
    """
    book_list = client.list_blobs(bucket_name)
    # for blob in book_list:
    #     print(blob.name)
    data = []
    for i in range(book_list):
        items= {i:i}
    # return book_list
    return json.dumps(data.append(items))


# @public_api.route("/read", methods=['GET'])
# def read():
#     # http://127.0.0.1:5000/public/read
#     """

#     :return:
#     """
#     return json.dumps({'success': True})


# view without downloading the file
def search_a_book(book_name):
    blob = bucket.get_blob(book_name)
    if blob is None:
        return json.dumps({'error': "Sorry, we do not have this book!"})
    else:
        return json.dumps({'success':True, 'book_name': '{}'.format(blob.name)})
