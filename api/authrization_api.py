import json

from flask import Blueprint, request
# from services.database.DBConn import database
from security.jwtSecurity import (session_cookie, public_cookie, gps)


# userDB = database.users
auth_api = Blueprint('auth_api', __name__)

@auth_api.route("/login")
def user_login():
    # access token  == usertoken
    """Generated End-Point Sample
    http://0.0.0.0:5000/auth/login?username=testuser1&password=password
    """
    username = request.args.get("username")
    password = request.args.get("password")
    authtoken = session_cookie(username).decode('utf-8')
    return json.dumps({'success': True, 'token': authtoken})



@auth_api.route("/p_access")
def public_access():
    # http://0.0.0.0:5000/auth/p_access
    """
    :return:
    """
    # access token  == p_access
    region = gps()
    if 'New York' not in region:
        return json.dumps({'error': "this website is designed only for New Yorker!"})
    else:
        p_token = public_cookie().decode('utf-8')
        return json.dumps({'success': True, 'p_token':p_token})

# if __name__ == "__main__":
#     print(gps())
