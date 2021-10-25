from configurations.load_config import load_config
from utils.setup_logger import setup_logger


def main():
    # Setup logging
    logger = setup_logger()

    # Load configurations
    logger.info("Loading configurations...")
    config = load_config()
    logger.info(f"Found configurations: {config}.")


if __name__ == "__main__":
    main()
