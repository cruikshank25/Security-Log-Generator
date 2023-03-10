import logging
import config


def ids_logger():
    logger = logging.getLogger('ids_logger_1')
    logging_level = config.logging_level
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/ids.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def access_logger():
    logger = logging.getLogger('access_logger_1')
    logging_level = config.logging_level
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/access.log')
    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def endpoint_logger():
    logger = logging.getLogger('endpoint_logger_1')
    logging_level = config.logging_level
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/endpoint.log')
    formatter = logging.Formatter('Date: %(asctime)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger