from models.config_classes import MonitorConfiguration, APIFetcherConfiguration
import yaml
import logging


logger = logging.getLogger("__name__")


def load_monitor_config(config_file_path: str) -> MonitorConfiguration:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            monitor_config = MonitorConfiguration(
                high_temp=configs["high_temp"],
                low_temp=configs["low_temp"],
                checking_frequency=configs["checking_frequency"],
                locations=configs["locations"],
            )

            return monitor_config

    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise error


def load_api_fetcher_config(config_file_path: str) -> APIFetcherConfiguration:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            # The config["locations"] are automatically
            # casted into Location objects
            api_fetcher_config = APIFetcherConfiguration(
                api_key=configs["api_key"]
            )

            return api_fetcher_config

    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise error
