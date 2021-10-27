from flask import json
from forecast import ForecastData
from typing import List, Dict
from sqlite3 import Connection, Error
from utils.database_utils import get_cnxn, execute_query


def get_forecasts(db_filepath: str) -> List[ForecastData]:
    cnxn = get_cnxn(db_filepath)
    result = get_all_forecast_table(cnxn)
    return json.dumps(result)


def insert_forecasts(db_filepath: str, forecasts: List[ForecastData]) -> None:
    for forecast in forecasts:
        cnxn = get_cnxn(db_filepath)
        insert_into_forecast_table(cnxn, forecast)


def get_all_forecast_table(cnxn: Connection) -> List[Dict]:
    query = """SELECT *
               FROM forecast"""
    forecasts = execute_query(cnxn, query)
    return forecasts


def insert_into_forecast_table(cnxn: Connection, forecast_data_row: ForecastData):
    query = """INSERT INTO forecast (lon, lat, high_temp, low_temp, exceeds_limits, timestamp)
               VALUES (?, ?, ?, ?, ?, ?)"""

    query_params = [
        forecast_data_row.lon,
        forecast_data_row.lat,
        forecast_data_row.high_temp,
        forecast_data_row.low_temp,
        forecast_data_row.exceeds_limits,
        forecast_data_row.timestamp,
    ]

    execute_query(cnxn, query, query_params)
