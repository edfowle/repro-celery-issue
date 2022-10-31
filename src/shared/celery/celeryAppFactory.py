from celery import Celery
from celery.signals import after_setup_logger
import os
import logging

setupLogPath = None

def createApp(name, brokerUrl, backendUrl, logPath):
    global setupLogPath
    setupLogPath = logPath
    return Celery('tasks', broker=brokerUrl, backend=backendUrl)

@after_setup_logger.connect
def setup_loggers(celeryLogger, **kwargs):
    global setupLogPath
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    os.makedirs(str(Path(path).parent), exist_ok=True)
    fh = logging.FileHandler(setupLogPath)
    fh.setFormatter(formatter)
    celeryLogger.addHandler(fh)