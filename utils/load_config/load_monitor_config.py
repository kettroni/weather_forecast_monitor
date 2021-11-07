import logging
import yaml
from models.config_classes import MonitorConfiguration, APIFetcherConfiguration
from models.data import MonitorData


logger = logging.getLogger("__name__")


def load_monitor_config(config_file_path: str) -> MonitorConfiguration:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            monitor_datas = []
            for loc, temp in zip(configs["locations"], configs["temp_limits"]):
                monitor_data = MonitorData(location=loc, temp_limit=temp)
                monitor_datas.append(monitor_data)

            monitor_config = MonitorConfiguration(
                checking_frequency=configs["checking_frequency"],
                monitor_datas=monitor_datas,
            )

            return monitor_config

    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise MonitorConfigurationError(error)

class MonitorConfigurationError(Exception):
    pass
