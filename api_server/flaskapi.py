"""
API server is started by running this file.
"""
from flask import Flask, request, jsonify, Response


api = Flask(__name__)


# Load all the predefined routes
import routes.forecast_routes

if __name__ == "__main__":
    api.run()
