import sqlite3
from sqlite3 import Connection


def initialize_database(db_filepath: str = "./database/forecastsqlite.db") -> None:
    """
    Initializes database with required tables.
    """
    try:
        cnxn = sqlite3.connect(db_filepath)
        create_forecast_table(cnxn)
        cnxn.close()
    except Exception as e:
        raise e


def create_forecast_table(cnxn: Connection) -> None:
    try:
        # Context manager automatically commits transactions.
        # If there is an exception the transactions are rolled back.
        with cnxn:
            query = """ CREATE TABLE IF NOT EXISTS forecast (
                            id integer PRIMARY KEY,
                            lon real NOT NULL,
                            lat real NOT NULL,
                            high_temp real NOT NULL,
                            low_temp real NOT NULL,
                            exceeds_limits integer NOT NULL,
                            timestamp text NOT NULL
                        );"""

            cnxn.execute(query)
    except sqlite3.Error as e:
        raise e

