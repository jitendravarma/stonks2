# importing module
import logging
from datetime import datetime

now = datetime.now()
# Create and configure logger
logging.basicConfig(filename='{:%Y-%m-%d}-concentration.log'.format(datetime.now()),
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
