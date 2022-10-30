from shared.logging import logger
import celery

BROKER_URL = 'redis://redis:6379/0'
BACKEND_URL = 'redis://redis:6379/1'
app = celery.Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, )

@app.task(name='Add two numbers')
def add(x, y):
    return x + y