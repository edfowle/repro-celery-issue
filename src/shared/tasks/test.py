from shared.logging import logger
logger.setup('/var/log/repro_celeryissue/tasks.test.log')

import celery

BROKER_URL = 'redis://redis:6379/0'
BACKEND_URL = 'redis://redis:6379/1'
app = celery.Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, )

@app.task(name='Throw an unhandled exception')
def add(x, y):
    raise Exception("oops")