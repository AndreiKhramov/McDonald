from celery import shared_task
import time

import logging
logger = logging.getLogger(__name__)

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")
