import logging
import yaml
from models.config_classes import APIFetcherConfiguration


logger = logging.getLogger("__name__")


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
        raise APIFetcherConfigurationError(error)

class APIFetcherConfigurationError(Exception):
    pass
