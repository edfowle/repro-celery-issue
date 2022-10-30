import logging
from shared.tasks import add

logging.info('calling task')
result = add.delay(66,4)
logging.info(f'task completed, {result}!')
