import os
import logging
import datetime
from pathlib import Path

setup_complete = False

def setup(path, level=logging.INFO):
    global setup_complete
    
    if(not setup_complete):
        setup_complete = True
        os.makedirs(str(Path(path).parent), exist_ok=True)
        logging.basicConfig(filename=path, level=level)

def info(message):
    logging.info(f'{datetime.datetime.now()}: {message}')