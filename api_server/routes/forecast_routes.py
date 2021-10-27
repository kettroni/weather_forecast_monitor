from __main__ import api, API_CONFIG
from controllers.forecast_controller import get_forecasts, insert_forecasts
from flask import request
from pydantic.error_wrappers import ValidationError
from forecast import ForecastData


@api.route("/forecasts", methods=["GET"])
def get_all_forecasts():
    forecasts = get_forecasts(API_CONFIG["DB_FILEPATH"])
    return forecasts, 200


@api.route("/forecasts", methods=["POST"])
def post_forecasts():
    req_json = request.get_json()
    try:
        forecasts = req_json["forecasts"]
        casted_forecasts = [ForecastData(**forecast) for forecast in forecasts]

        if len(casted_forecasts) > 0:
            insert_forecasts(API_CONFIG["DB_FILEPATH"], casted_forecasts)
            return "Created forecast succesfully.", 201
        else:
            return "Value in key 'forecast' is an empty list.", 400
    except KeyError as e:
        return "Key 'forecasts' missing from the request.", 400
    except TypeError as e:
        return str(e), 400
    except ValidationError as e:
        return str(e), 400
