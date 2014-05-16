import logging
from tasks import bogus
from celinit import celery_app
from log import setup_event_listening

logging.basicConfig(level=logging.INFO)
setup_event_listening(celery_app)
bogus.delay().get()
