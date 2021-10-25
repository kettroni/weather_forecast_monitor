import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(
    log_path: str = "./logs/monitor.log",
    fh: bool = True,
    ch: bool = True,
) -> logging.Logger:

    # Setup basic logging formats
    logging.basicConfig(
        format="[%(asctime)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    logger = logging.getLogger("")

    # Add file handler
    if fh:
        file_handler = TimedRotatingFileHandler(filename=log_path, when="midnight")
        logger.addHandler(file_handler)

    # Add console handler
    if ch:
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)

    return logger
