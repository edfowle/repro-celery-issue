import os
import logging
import datetime
from pathlib import Path

logger = logging.getLogger()

def setup(path, level=logging.INFO):
    global logger
    logger.setLevel(level)

def setupCustom(customLogger):
    global logger
    logger = customLogger

def setupFile(path, level=logging.INFO):
    global logger
    os.makedirs(str(Path(path).parent), exist_ok=True)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler(path)
    fh.setFormatter(formatter)
    fh.setLevel(level)
    logger.addHandler(fh)