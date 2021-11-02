from configurations.load_config import load_monitor_config, load_api_fetcher_config
from utils.setup_logger import setup_logger
from models.openweather_fetcher import OpenweatherFetcher
from models.our_api_sender import OurApiSender
from models.forecast_monitor import ForecastMonitor


def main():
    # Setup logging
    logger = setup_logger(log_path="./logs/monitor.log")

    # Load configurations
    monitor_config = load_monitor_config("./config.yaml")
    api_fetcing_config = load_api_fetcher_config("./config.yaml")

    # Create an instance of APIFetcher
    api_fetcher = OpenweatherFetcher(api_fetcing_config)

    # Create an instance of APISender
    api_sender = OurApiSender()

    # Initialize the monitor
    monitor = ForecastMonitor(monitor_config, api_fetcher, api_sender, logger)

    monitor.run()


if __name__ == "__main__":
    main()