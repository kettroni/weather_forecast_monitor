"""
This file includes table creation queries.
"""
CREATE_FORECAST_TABLE = """CREATE TABLE IF NOT EXISTS forecast (
                               id integer PRIMARY KEY,
                               lon real NOT NULL,
                               lat real NOT NULL,
                               high_temp real NOT NULL,
                               low_temp real NOT NULL,
                               exceeds_limits integer NOT NULL,
                               timestamp text NOT NULL
                           );"""
