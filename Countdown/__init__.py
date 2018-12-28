import logging


def create_logger(name):
    logger = logging.getLogger(name)
    h, f = logging.StreamHandler(), logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s')
    h.setFormatter(f)
    h2 = logging.FileHandler('Countdown.log')
    h2.setFormatter(f)
    logger.addHandler(h)
    logger.addHandler(h2)
    logger.setLevel(logging.DEBUG)
    return logger
