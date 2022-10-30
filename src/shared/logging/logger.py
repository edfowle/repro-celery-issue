import os
import logging
import datetime

setup_complete = false

def setup(path, level=logging.INFO):
    if(setup_complete):
        return
    setup_complete = true
    os.makedirs('/var/log/repro_celeryissue', exist_ok=True)
    logging.basicConfig(filename="/var/log/repro_celeryissue/producer.log", level=logging.INFO)

def info(message):
    logging.info(f'{datetime.datetime.now()}: {message}')

