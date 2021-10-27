import yaml
import logging
from typing import List, Dict

logger = logging.getLogger("__name__")


def load_api_config(config_file_path: str = "./config.yaml") -> List[Dict]:
    try:
        with open(config_file_path, "r") as yaml_file:
            configs = yaml.safe_load(yaml_file)

            return configs

    except IOError as io_error:
        logger.error(io_error)
        raise io_error
    except Exception as error:
        logger.error(error)
        raise error
