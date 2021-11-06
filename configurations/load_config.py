from models.config_classes import MonitorConfiguration, APIFetcherConfiguration
from models.monitor_target import MonitorTarget
import yaml
import logging


logger = logging.getLogger("__name__")


def load_monitor_config(config_file_path: str) -> MonitorConfiguration:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            monitor_targets = []
            for loc, temp in zip(configs["locations"], configs["temp_limits"]):
                monitor_target = MonitorTarget(location=loc, temp_limit=temp)
                monitor_targets.append(monitor_target)

            monitor_config = MonitorConfiguration(
                checking_frequency=configs["checking_frequency"],
                monitor_targets=monitor_targets,
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
            api_fetcher_config = APIFetcherConfiguration(api_key=configs["api_key"])
            return api_fetcher_config
    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise error
