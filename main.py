import os
from flask import Flask
from flask_cors import CORS

from api.secure_api import secure_api
from api.public_api import public_api
from api.authrization_api import auth_api


app = Flask(__name__)
CORS(app)
#All endpoints in public_api.py are prefixed with the /public route.
app.register_blueprint(public_api, url_prefix='/public')
#All endpoints in secure_api.py are prefixed with the /secure route.
app.register_blueprint(secure_api, url_prefix='/secure')
#All endpoints in authrization_api.py are prefixed with the /auth route.
app.register_blueprint(auth_api, url_prefix='/auth')


# root
@app.route("/", methods=['GET'])
def helloWorld():
    print("hello")
    return "Welcome To NYC Libray, you can add, search and read books here."


if __name__ == "__main__":
    # http://127.0.0.1:5000/
    app.run(port=5000, debug=True, host='0.0.0.0')
