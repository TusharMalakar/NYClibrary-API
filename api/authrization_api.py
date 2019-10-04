import json
from flask import Blueprint, request
from services.database.DBConn import database
from security.jwtSecurity import session_cookie


userDB = database.users
auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/login", methods=['GET'])
def user_login():
    """Generated End-Point Sample
    http://127.0.0.1:5000/auth/login?email=testuser12&password=password
    """
    email = request.args.get("email")
    password = request.args.get("password")
    if not email:
        return json.dumps({'error': "Email not provided.", 'success': False, 'code': 66})
    if not password:
        return json.dumps({'error': "Password not provided.", 'success': False, 'code': 67})

    record = userDB.find_one({'email':email})
    if record is None:
        return json.dumps({'error': "User doesn't exist.", 'success': False, 'code': 1})
    else:
        actualPassword = record['password']
        print(password," = ", actualPassword)
        if password == actualPassword:
            authtoken = session_cookie(email).decode("utf-8")
            return json.dumps({'success': True, 'token': authtoken})
        else:
            return json.dumps({'error': 'Invalid Password', 'code': 2})
