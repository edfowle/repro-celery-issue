import os
import logging
import datetime

setup_complete = False

def setup(path, level=logging.INFO):
    global setup_complete
    if(setup_complete):
        return
    setup_complete = True
    os.makedirs('/var/log/repro_celeryissue', exist_ok=True)
    logging.basicConfig(filename="/var/log/repro_celeryissue/producer.log", level=logging.INFO)

def info(message):
    logging.info(f'{datetime.datetime.now()}: {message}')

