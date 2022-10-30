import os
import logging
import datetime
from pathlib import Path

setup_complete = False

def setup(path, level=logging.INFO):
    global setup_complete
    
    info("configuring logging")
    if(setup_complete):
        info("already set up!")
        return
    setup_complete = True
    os.makedirs(str(Path(path).parent), exist_ok=True)
    logging.basicConfig(filename=path, level=logging.INFO)

def info(message):
    logging.info(f'{datetime.datetime.now()}: {message}')

