import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(
    log_path: str,
    msg_format: str = "[%(asctime)s][%(levelname)s] - %(message)s",
    console_handler: bool = True,
) -> logging.Logger:

    logging.basicConfig(
        filename=log_path,
        filemode="w",
        format=msg_format,
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    logger = logging.getLogger(__name__)

    # Add console handler
    if console_handler:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(msg_format))
        logger.addHandler(console_handler)

    return logger
