import logging
import sys

# Configure basic logging
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="app.log",
        filemode="a"
    )

    # Get logger instance
    logger = logging.getLogger(__name__)
    return logger
