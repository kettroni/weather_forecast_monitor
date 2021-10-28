from configurations.load_config import load_monitor_config
from utils.setup_logger import setup_logger


def main():
    pass


if __name__ == "__main__":
    # Setup logging
    logger = setup_logger()

    # Load configurations
    logger.info("Loading configurations...")
    config = load_monitor_config()
    logger.info(f"Found configurations: {config}.")
    main()
