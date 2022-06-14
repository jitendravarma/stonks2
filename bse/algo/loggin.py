# importing module
import logging
from datetime import datetime

now = datetime.now()
# Create and configure logger


def get_logger(dir_path=""):
    file_name = '{:%Y-%m-%d}-concentration.log'.format(
        datetime.now())
    file_name = f'{dir_path}{file_name}'
    logging.basicConfig(filename=file_name,
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    return logger
