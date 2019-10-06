import os
import json
import hashlib

from services.database.DBConn import database
from flask import Blueprint, request
from services.database.DBConn import (bucket, client, bucket_name)



userDB = database.users
public_api = Blueprint('public_api', __name__)


@public_api.route("/create_user", methods=['POST'])
def createUser():
    """
    #http://127.0.0.1:5000/public/create_user
    body = {
	"email":"example@gmail.com",
	"password":"password123"
    }
    :return: {"success": false, "error": "User already exist."}
            or  {"success": True, 'message': 'you can log-in now, using usename and password'}
    """

    body = request.get_json()
    email = body['email']
    password = body['password']
    print(email, password)

    if not email:
        return json.dumps({'error': "Email parameter was not provided.", 'code': 1})
    if not password:
        return json.dumps({'error': "Password parameter was not provided.", 'code': 2})
    if len(password) < 6 or len(password) > 52:
        return json.dumps({'error': "Password must be at least 6 characters and less than 52 characters long.", 'code': 3})
    record = userDB.find_one({'email': email}, {'_id': 1})

    if record is None:
        # hashed_password = hash_a_string(password)
        # result = userDB.insert_one({"email":email,"password":hashed_password})

        result = userDB.insert_one({"email":email,"password":password})
        return json.dumps({"success": True, 'message': 'you can log-in now, using usename and password'})
    else:
        return json.dumps({"success": False, 'error':'User already exist.'})


@public_api.route("/search", methods=['GET'])
def search():
    # http://127.0.0.1:5000/public/search?book_name=FALL2019.PNG
    book_name = request.args.get('book_name')
    status = search_a_book(book_name)
    return status


# view without downloading the file
def search_a_book(book_name):
    blob = bucket.get_blob(book_name)
    if blob is None:
        return json.dumps({'error': "file not found"})
    else:
        return json.dumps({'success':True, 'book_name': '{}'.format(blob.name)})


# encrypting a string with salt
def hash_a_string(str):
    salt = os.urandom(32).hex()
    hashy = hashlib.sha512()
    hashy.update(('%s%s' % (salt, str)).encode('utf-8'))
    hashed_str = hashy.hexdigest()
    return hashed_str


@public_api.route("/book_list", methods=['GET'])
def list_of_books():
    """
    :param: None
    :return: list of all available books
    """
    book_list = client.list_blobs(bucket_name)
    list = []
    try:
        for value in book_list:
            book = value.name
            list.append(book)
        return json.dumps(list)
    except Exception as e:
        print(e)
        return json.dumps({'error': "No value found"})


##################################################################################


# @public_api.route("/download_book", methods =['GET'])
# def download_a_book():
#     book_name = request.args.get('book_name')
#     book = download_book(book_name)
#     return json.dumps({'book':book})


# def download_book(file_name):
#     """Downloads a blob from the bucket."""
#     blob = bucket.blob(file_name)
#     blob.download_to_filename(file_name)



# def download_blob(bucket_name, source_blob_name, destination_file_name):
#     """Downloads a blob from the bucket."""
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)
#
#     blob.download_to_filename(destination_file_name)
#
#     print('Blob {} downloaded to {}.'.format(
#         source_blob_name,
#         destination_file_name))


# @public_api.route("/forget_pass")
# def reset_password():
#     request.args.get('email')
#     # send a conformation number to enter
#     pass
#
#
# @public_api.route("/send_email")
# def send_conformaintion_num():
#     pass
#
#
# @public_api.route("/get_conformation")
# def get_conformation_number():
#     pass


# @public_api.route("/read", methods=['GET'])
# def read():
#     # http://127.0.0.1:5000/public/read
#     """

#     :return:
#     """
#     return json.dumps({'success': True})




# def send_email(email, message):
#     pass
