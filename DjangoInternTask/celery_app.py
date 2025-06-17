import os
from celery import Celery

# Set default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoInternTask.settings')

# Create Celery app
app = Celery('DjangoInternTask')

# Load settings from Django settings file using 'CELERY_' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all registered Django apps
app.autodiscover_tasks()