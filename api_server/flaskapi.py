"""
API server is started by running this file.
"""
from flask import Flask, session
from utils.database_utils import initialize_database
from utils.load_api_config import load_api_config

# Load API configurations
API_CONFIG = load_api_config()

# Initialize flask object
api = Flask(__name__)

# Load all the predefined routes
import routes.forecast_routes

if __name__ == "__main__":
    # Set logger level
    api.logger.setLevel("DEBUG")

    # Configurations
    api.logger.info(f"Starting server with the following configurations: {API_CONFIG}")

    # Initialize database
    api.logger.info(f"Initializing database in '{API_CONFIG['DB_FILEPATH']}'...")
    initialize_database(API_CONFIG["DB_FILEPATH"])
    api.logger.info("Database created.")

    # Run the API server
    api.run()
