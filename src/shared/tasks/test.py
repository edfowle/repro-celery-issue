from shared.celery import celeryAppFactory

app = celeryAppFactory.createApp('tasks', 'redis://redis:6379/0', 'redis://redis:6379/1', '/var/log/repro_celeryissue/celery.tasks.test.log')

@app.task(name='Throw an unhandled exception')
def add(x, y):
    raise Exception("oops")