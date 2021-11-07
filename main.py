"""
This main module can run any ForecastMonitor implementation, which are defined
inside "./monitors/forecast_monitor/". This example is using the open_weather_map_monitor implementation.
"""
from datetime import datetime
from utils.load_config import load_monitor_config
from utils import setup_logger
from monitors.forecast_monitor import ForecastMonitor
from monitors.forecast_monitor.open_weather_map_monitor import get_fetcher, get_sender


def main():
    # Setup logging
    start_time = datetime.now().strftime("%d-%m-%y_%H:%M:%S")
    logger = setup_logger(log_path=f"./logs/{start_time}.log")

    # Load monitor configurations
    monitor_config = load_monitor_config("./monitor_config.yaml")

    # Get an instance of APIFetcher
    api_fetcher = get_fetcher()

    # Create an instance of APISender
    api_sender = get_sender()

    # Initialize the monitor
    monitor = ForecastMonitor(monitor_config, api_fetcher, api_sender, logger)
    monitor.run()


if __name__ == '__main__':
    main()
