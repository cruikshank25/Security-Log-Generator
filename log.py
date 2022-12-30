import logging
import config

def custom_logger():
    logger = logging.getLogger('security_logger_1')
    logging_level = config.logging_level
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('security.log')
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


