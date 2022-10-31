from shared.celery import celeryAppFactory
from shared.logging import loggingWrapper

app = celeryAppFactory.createApp('tasks', 'redis://redis:6379/0', 'redis://redis:6379/1', '/var/log/repro_celeryissue/celery.tasks.test.log')

@app.task(name='Throw an unhandled exception')
def process(i):
    loggingWrapper.logger.info(f'processing task {i}')
    raise Exception(f'oops - task {i} failed')