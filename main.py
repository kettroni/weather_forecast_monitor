from configurations.load_config import load_monitor_config, load_api_fetcher_config
from utils.setup_logger import setup_logger
from models.openweather_fetcher import OpenweatherFetcher
from models.our_api_sender import OurApiSender
from models.forecast_monitor import ForecastMonitor
from datetime import datetime


def main():
    # Setup logging
    start_time = datetime.now().strftime("%d-%m-%y_%H:%M:%S")
    logger = setup_logger(log_path=f"./logs/{start_time}.log")

    # Load configurations
    config_path = "./config.yaml"
    monitor_config = load_monitor_config(config_path)
    api_fetcing_config = load_api_fetcher_config(config_path)

    # Create an instance of APIFetcher
    api_fetcher = OpenweatherFetcher(api_fetcing_config)

    # Create an instance of APISender
    api_sender = OurApiSender("http://127.0.0.1:5000/forecasts")

    # Initialize the monitor
    monitor = ForecastMonitor(monitor_config, api_fetcher, api_sender, logger)
    monitor.run()


if __name__ == "__main__":
    main()
