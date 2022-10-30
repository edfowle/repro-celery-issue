from shared.logging import logger
import celery

BROKER_URL = 'redis://redis:6379/0'
BACKEND_URL = 'redis://redis:6379/1'
app = celery.Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, )

logger.setup('/var/log/repro_celeryissue/tasks.test.log')

@app.task(name='Add two numbers')
def add(x, y):
    logger.info('started task')
    result = x + y
    logger.info('finished task')
    return result