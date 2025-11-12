import logging


log = logging.getLogger(__name__)

formatter = logging.Formatter(
    "[VOLK {asctime}]: {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_logger = logging.StreamHandler()
console_logger.setFormatter(fmt=formatter)
log.addHandler(console_logger)
log.setLevel(logging.INFO)
