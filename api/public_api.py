import os, json, hashlib
import security.jwtSecurity
from services.database.DBConn import database
from flask import Blueprint, request
from services.database.DBConn import (bucket, client, bucket_name)


userDB = database.users
public_api = Blueprint('public_api', __name__)


@public_api.route("/search", methods=['GET'])
def search():
    # http://127.0.0.1:5000/public/search?book_name=3.txt
    book_name = request.args.get('book_name')
    status = search_a_book(book_name)
    return status


# @public_api.route("/download_book", methods =['GET'])
# def download_a_book():
#     book_name = request.args.get('book_name')
#     book = download_book(book_name)
#     return json.dumps({'book':book})


@public_api.route("/createUser", methods=['PUT'])
def createUser():
    # http://127.0.0.1:5000/public/createUser
    email = request.args.get('email')
    password = request.agrs.get('password')
    if not email:
        return json.dumps({'error': "Email parameter was not provided.", 'code': 1})
    if not password:
        return json.dumps({'error': "Password parameter was not provided.", 'code': 2})
    
    email = email.lower()
    if "@" not in email:
        return json.dumps({'error': "email is not a valid email.", 'code': 3})
    if email[-18:] != "@myhunter.cuny.edu":
        return json.dumps({'error': "Email is not a valid @myhunter.cuny.edu email.", 'code': 4})
    if email[:-18] == "":
        return json.dumps({'error': "@myhunter.cuny.edu email is invalid.", 'code': 5})

    if len(password) < 6 or len(password) > 52:
        return json.dumps({'error': "Password must be at least 6 characters and less than 52 characters long.", 'code': 6})

    salt = os.urandom(32).hex()
    hashy = hashlib.sha512()
    hashy.update(('%s%s' % (salt, password)).encode('utf-8'))
    hashed_password = hashy.hexdigest()
    try:
        record = userDB.find_one({'email': email}, {'_id': 1})
        if record is None:
            user = {'email': email, 'salt': salt, 'password': hashed_password}
            result = userDB.insert_one(user)
            if result.inserted_id:
                # print("created new user: " + email)
                authtoken = security.jwtSecurity.session_cookie(email).decode("utf-8")
                return json.dumps({'success': True, 'token': authtoken})
            else:
                return json.dumps({'error': "Server error while creating new user.", 'code': 7})
        else:
            return json.dumps({'error': "User already exists.", 'code': 8})
    except Exception as e:
        print(e)
        return json.dumps({'error': "Server error while checking if email already exists.", 'code': 9})


@public_api.route("/forget_pass")
def reset_password():
    request.args.get('email')
    # send a conformation number to enter
    pass


@public_api.route("/send_email")
def send_conformaintion_num():
    pass


@public_api.route("/get_conformation")
def get_conformation_number():
    pass


# def download_book(file_name):
#     """Downloads a blob from the bucket."""
#     blob = bucket.blob(file_name)
#     blob.download_to_filename(file_name)


# @public_api.route("/book_list", methods=['GET'])
# def list_of_books():
#     """
#     :return: iterable_object
#     """
#     book_list = client.list_blobs(bucket_name)
#     # for blob in book_list:
#     #     print(blob.name)

#     # NB: Create a json file bofore return
#     return book_list


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


def send_email(email, message):
    pass
