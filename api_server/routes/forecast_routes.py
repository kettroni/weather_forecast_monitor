from __main__ import api
from controllers.forecast_controller import get_forecasts, insert_forecasts
from flask import Response, request
from pydantic.error_wrappers import ValidationError
from forecast import ForecastData


@api.route("/forecasts", methods=["GET"])
def get_all_forecasts():
    forecasts = get_forecasts()

    return forecasts


@api.route("/forecasts", methods=["POST"])
def post_forecast():
    req_json = request.get_json()
    try:
        forecasts = req_json["forecasts"]
        casted_forecasts = [ForecastData(**forecast) for forecast in forecasts]
        
        insert_forecasts(casted_forecasts)
        return "Created forecast succesfully.", 201
    except TypeError as e:
        return str(e), 400
    except KeyError as e:
        return "Key 'forecasts' missing from the request.", 400
    except ValidationError as e:
        return str(e), 400