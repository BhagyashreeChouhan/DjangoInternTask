from .celery_app import app as celery_app

# Make Celery app available for Django imports
__all__ = ('celery_app',)