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


class Fibonacci:
    def __init__(self):
        self._call = 0
        self._first = 0
        self._second = 1

    def next(self):
        self._call += 1

        if self._call == 1:
            return {"call": 1, "value": 0}

        if self._call == 2:
            return {"call": 2, "value": 1}

        next_value = self._first + self._second

        self._first = self._second
        self._second = next_value

        return {"call": self._call, "value": next_value}


FIBONACCI = Fibonacci()


@APP.route("/fibonacci")
def fibonacci():
    return FIBONACCI.next(), 200


if __name__ == "__main__":
    APP.run(debug=True, host="0.0.0.0", port=8080)
