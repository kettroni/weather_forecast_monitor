import sqlite3
from sqlite3 import Connection
from typing import List, Dict, Callable
from utils.create_tables import CREATE_FORECAST_TABLE


# You can set this list of functions (which create tables)
# to be called when initializing database
CREATE_TABLE_QUERIES = [CREATE_FORECAST_TABLE]


def initialize_database(
    db_filepath: str, queries: List[str] = CREATE_TABLE_QUERIES
) -> None:
    """
    Initializes database with required tables.
    """
    cnxn = get_cnxn(db_filepath)
    try:
        for query in queries:
            execute_query(cnxn, query)
    except Exception as e:
        raise e


def get_cnxn(db_filepath: str) -> Connection:
    try:
        cnxn = sqlite3.connect(db_filepath)

        # Cursors
        cnxn.row_factory = sqlite3.Row
        return cnxn
    except Exception as e:
        raise e


def execute_query(cnxn: Connection, query: str, query_params: str = "") -> None:
    cursor = cnxn.cursor()
    try:
        # Context manager automatically commits transactions.
        # If there is an exception the transactions are rolled back.
        with cnxn:
            cursor.execute(query, query_params)
    except sqlite3.Error as e:
        raise e

    result = [dict(row) for row in cursor.fetchall()]
    return result
