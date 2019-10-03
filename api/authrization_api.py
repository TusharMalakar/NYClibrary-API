import hashlib
import json
import os

from flask import Blueprint, request
from services.database.DBConn import database
from security.jwtSecurity import (session_cookie, public_cookie, gps)


userDB = database.users
auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/login", methods=['GET'])
def user_login():
    """Generated End-Point Sample
    https://nyclibrary-api.appspot.com/auth/login?email=email01&password=password
    """
    username = request.args.get("email")
    password = request.args.get("password")
    if not username:
        return json.dumps({'error': "Username not provided.", 'success': False, 'code': 66})
    if not password:
        return json.dumps({'error': "Password not provided.", 'success': False, 'code': 67})

    username = username.lower()

    try:
        record = userDB.find_one({'username': username})
        if record is None:
            return json.dumps({'error': "User doesn't exist.", 'success': False, 'code': 1})
        else:
            actualPassword = record['password']

            # Fix pre-encrypted accounts.
            if 'salt' not in record:
                newSalt = os.urandom(32).hex()
                newhashy = hashlib.sha512()
                newhashy.update(('%s%s' % (newSalt, actualPassword)).encode('utf-8'))
                newhashed_password = newhashy.hexdigest()
                userDB.update_one(
                    {"username": username},
                    {
                        "$set": {
                            "salt": newSalt,
                            "password": newhashed_password
                        }
                    }
                )
                record['salt'] = newSalt;
                actualPassword = newhashed_password;

            salt = record['salt']
            hashy = hashlib.sha512()
            hashy.update(('%s%s' % (salt, password)).encode('utf-8'))
            hashed_password = hashy.hexdigest()

            if hashed_password == actualPassword:
                authtoken = session_cookie(username).decode("utf-8")
                return json.dumps({'success': True, 'token': authtoken})
            else:
                return json.dumps({'error': 'Invalid Password', 'code': 2})
    except Exception as e:
        print(e)
        return json.dumps({'error': "Server error while checking if user exists.", 'code': 3})


@auth_api.route("/p_access", methods=['GET'])
def public_access():
    # http://127.0.0.1:5000/auth/p_access
    """
    :return:
    """
    region = gps()
    if 'New York' not in region:
        return json.dumps({'error': "this website is designed only for New Yorker!"})
    else:
        p_token = public_cookie().decode('utf-8')
        return json.dumps({'success': True, 'p_token':p_token})

# if __name__ == "__main__":
#     print(gps())
