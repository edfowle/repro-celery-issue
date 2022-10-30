from shared.tasks import test
from shared.logging import logger

logger.setup('/var/log/repro_celeryissue/producer.log')

logger.info('queueing task')
result = test.add.delay(66,4)
logger.info('task queued')