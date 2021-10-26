"""
API server is started by running this file.
"""
from flask import Flask
from database.database_utils import initialize_database


api = Flask(__name__)

# Load all the predefined routes
import routes.forecast_routes

if __name__ == "__main__":
    # Set logger level
    api.logger.setLevel("DEBUG")

    # Initialize database
    api.logger.info("Initializing database...")
    initialize_database()
    api.logger.info("Database created.")

    # Run the API server
    api.run()

