import os
import logging
import datetime

def setup(path, level=logging.INFO):
    os.makedirs('/var/log/repro_celeryissue', exist_ok=True)
    logging.basicConfig(filename="/var/log/repro_celeryissue/producer.log", level=logging.INFO)

def info(message):
    logging.info(f'{datetime.datetime.now()}: {message}')

