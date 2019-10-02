import os
import jwt
import requests
import datetime

from functools import wraps
from flask import request, Response

key = "ThisIsAVeryBadAPISecretKeyThatIsOnlyUsedWhenRunningLocally"
if 'API_KEY' in os.environ: SECRET_KEY = os.environ['API_KEY']


def gps():
    # Step 1) Find the public IP of the user. This is easier said that done, look into the library Netifaces if you're
    # interested in getting the public IP locally.
    # The GeoIP API I'm going to use here is 'https://geojs.io/' but any service offering similar JSON data will work.

    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}


    # Step 2) Look up the GeoIP information from a database for the user's ip

    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    region = geo_data['region']
    return region


def session_cookie(username):
    """
    :param  username:
    :return: a session_cookie for 5 minutes for a user
    """
    try:
        payload = {
           'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'username': username
        }
        session_cookies = jwt.encode(payload, key, algorithm='HS256')
        return session_cookies

    except Exception as e:
        return e


def public_cookie():
    # access token  == p_access
    region = gps()
    try:
        payload = {'region':region}
        p_access =  jwt.encode(payload, key, algorithm='HS256')
        return p_access

    except Exception as e:
        return e


def public_access_decoder(p_cookie):
    """
    :param p_cookie:
    :return: validity of p_cookie
    """
    try:
        payload = jwt.decode(p_cookie, key)
        return 'SUCCESS' + payload['region']
    except jwt.InvalidTokenError:
        return 'Invalid token'


def cookie_decoder(cookie):
    """
    :param cookie:
    :return: validity of cookie
    """
    try:
        payload = jwt.decode(cookie, key)
        return 'SUCCESS' + payload['username']
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

        username = cookie_decoder(auth_token)

        if username.startswith('SUCCESS'):
            request.userNameFromToken = username[7:]
            return function(*args, **kwargs)
        else:
            return Response('\n' 'You have to login with proper credentials', 401,
                            {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return decorated



def requires_nyc_auth():
    pass





# if __name__ == "__main__":
#     print(session_cookie("hi"))
#
