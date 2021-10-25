"""
API server is started by running this file.
"""
from flask import Flask, json
from methods.get_methods import get_forecasts
from methods.post_methods import post_forecasts


api = Flask(__name__)


# All routes defined here, must use wrapper functions
# for correct importing from external module.
@api.route("/forecasts", methods=["GET"])
def wrapper_one():
    return get_forecasts()


@api.route("/forecasts", methods=["PUSH"])
def wrapper_two():
    return post_forecasts()


if __name__ == "__main__":
    api.run()
