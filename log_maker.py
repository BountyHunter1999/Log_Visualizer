import logging
import random

logging.basicConfig(
    filename="logFile.log",
    filemode="a",
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

for i in range(0, 15):
    x = random.randint(0, 2)
    if x == 0:
        logging.warning("Warning Log Message")
    elif x == 1:
        logging.critical("Critical Log Message")
    else:
        logging.error("Error Log Message")
