from shared.logging import logger
logger.setup('/var/log/repro_celeryissue/producer.log')

from shared.tasks import test
logger.info('queueing task')
result = test.add.delay(66,4)
logger.info('task queued')