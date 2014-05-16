import logging
from celery.signals import after_setup_logger
from celery.signals import after_setup_task_logger
from log import TaskLogEmitter
from celinit import celery_app

worker_logger = logging.getLogger(__name__)
worker_logger.setLevel(logging.INFO)


@after_setup_logger.connect
@after_setup_task_logger.connect
def setup_task_log_emitter(logger=None, **kwargs):
    """
    setup log handler
    """
    handler = TaskLogEmitter(celery_app)
    logger.addHandler(handler)


@celery_app.task
def bogus():
    worker_logger.info("info from task")
    worker_logger.warning("warning from task")
    worker_logger.error("error from task")
    worker_logger.debug("debug from task")
    return "love"
