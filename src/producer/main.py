import logging
import os
from shared.tasks import add
os.makedirs('/var/log/repro_celeryissue', exist_ok=true)
logging.basicConfig(filename="/var/log/repro_celeryissue/producer.log", level=logging.INFO)

logging.info('calling task')
result = add.delay(66,4)
logging.info(f'task completed, {result}!')
