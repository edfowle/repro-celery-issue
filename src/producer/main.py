from shared.logging import loggingWrapper
loggingWrapper.setupFile('/var/log/repro_celeryissue/producer.log')

from shared.tasks import test

n = 10000

loggingWrapper.logger.info(f'queueing {n} tasks')

i = 0
while i < n:
  result = test.process.delay(n)
  i += 1

loggingWrapper.logger.info('tasks queued')