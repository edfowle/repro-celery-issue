from celery import Celery
from celery.signals import after_setup_logger
from shared.logging import loggingWrapper
import os
import logging
from pathlib import Path

setupLogPath = None

def createApp(name, brokerUrl, backendUrl, logPath):
    global setupLogPath
    setupLogPath = logPath
    return Celery('tasks', broker=brokerUrl, backend=backendUrl)

@after_setup_logger.connect
def setup_loggers(logger, **kwargs):
    global setupLogPath

    loggingWrapper.setupCustom(logger)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    os.makedirs(str(Path(setupLogPath).parent), exist_ok=True)
    fh = logging.FileHandler(setupLogPath)
    fh.setFormatter(formatter)
    logger.addHandler(fh)