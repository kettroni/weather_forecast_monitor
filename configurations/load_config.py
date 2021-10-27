from .config_classes import MonitorConfiguration
import yaml
import logging


logger = logging.getLogger("__name__")


def load_monitor_config(config_file_path: str = "./config.yaml") -> MonitorConfiguration:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            # The config["locations"] are automatically 
            final_config = MonitorConfiguration(
                locations=configs["locations"],
                high_temp=configs["high_temp"],
                low_temp=configs["low_temp"],
                checking_frequency=configs["checking_frequency"]
            )

            return final_config

    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise error

