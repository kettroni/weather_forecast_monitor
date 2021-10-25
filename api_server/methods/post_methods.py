from flask import json


forecasts = [{"id": 1, "name": "Forecast One"}, {"id": 2, "name": "Forecast Two"}]


def get_forecasts():
    return json.dumps(forecasts)
