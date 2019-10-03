import os
import jwt
import datetime

from functools import wraps
from flask import request, Response

key = "ThisIsAVeryBadAPISecretKeyThatIsOnlyUsedWhenRunningLocally"
if 'API_KEY' in os.environ: SECRET_KEY = os.environ['API_KEY']


def session_cookie(email):
    """
    :param  email:
    :return: a session_cookie for 5 minutes for a user
    """
    try:
        payload = {
           'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'email': email
        }
        session_cookies = jwt.encode(payload, key, algorithm='HS256')
        return session_cookies

    except Exception as e:
        return e


def cookie_decoder(cookie):
    """
    :param cookie:
    :return: validity of cookie
    """
    try:
        payload = jwt.decode(cookie, key)
        return 'SUCCESS' + payload['email']
    except jwt.ExpiredSignatureError:
        return 'Signature is expired. Please log in again'
    except jwt.InvalidTokenError:
        return 'Invalid token, Please log in with proper credentials'


def requires_auth(function):
    """
    :param function:
    :return: the validity of a request
    """
    @wraps(function)
    def decorated(*args, **kwargs):
        p_access = False
        auth_token = False
        if not auth_token:
            auth_token = request.header.get('Authorization')
        if not auth_token:
            return Response('Missing Auth Token!\n' 'You have to login with proper credentials', 401,
                            {'WWW-Authenticate': 'Basic realm="Login Required"'})

        email = cookie_decoder(auth_token)

        if email.startswith('SUCCESS'):
            request.userNameFromToken = email[7:]
            return function(*args, **kwargs)
        else:
            return Response('\n' 'You have to login with proper credentials', 401,
                            {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return decorated


# if __name__ == "__main__":
#     print(session_cookie("hi"))
#
