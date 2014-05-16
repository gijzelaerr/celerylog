from celery import Celery

broker = 'amqp://guest@localhost//'

celery_app = Celery('tasks', broker=broker, backend=broker)