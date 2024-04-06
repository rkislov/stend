from celery import Celery

app = Celery('stend', broker_url='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks = True