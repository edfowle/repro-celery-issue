from shared.logging import loggingWrapper
loggingWrapper.setup('/var/log/repro_celeryissue/producer.log')

from shared.tasks import test
loggingWrapper.logger.info('queueing task')
result = test.add.delay(66,4)
loggingWrapper.logger.info('task queued')