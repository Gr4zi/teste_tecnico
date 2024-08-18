import logging
import time
import random

logging.basicConfig(filename='/var/log/myapp.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

while True:
    log_level = random.choice([logging.INFO, logging.WARNING, logging.ERROR])
    logging.log(log_level, 'Este é um log de nível %s', log_level)
    time.sleep(5)