import logging


def ids_logger(logging_level):
    logger = logging.getLogger('ids_logger_1')
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/ids.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def access_logger(logging_level):
    logger = logging.getLogger('access_logger_1')
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/access.log')
    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def endpoint_logger(logging_level):
    logger = logging.getLogger('endpoint_logger_1')
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler('logs/endpoint.log')
    formatter = logging.Formatter('Date: %(asctime)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger