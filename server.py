import os
import uuid
from datetime import datetime

from flask import Flask
from flask_restful import Api

'''Simple REST service
'''

APP = Flask(__name__)
API = Api(APP)


@APP.route("/infos")
def infos():
    return {
               "timestamp": str(datetime.now()),
               "pid": os.getpid(),
               "loadavg": os.getloadavg()
           }, 200


@APP.route("/randoms")
def randoms():
    return {
               "timestamp": str(datetime.now()),
               "random": str(uuid.uuid4())
           }, 200


@APP.route("/echo/<string:number>")
def echo(number):
    return {"data": number}, 200


if __name__ == "__main__":
    APP.run(debug=True, host="0.0.0.0", port=8080)
