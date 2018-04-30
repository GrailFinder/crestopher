CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Makassar'
CELERY_BEAT_SCHEDULE = {}

from celery.schedules import crontab

# Other Celery settings
CELERY_BEAT_SCHEDULE = {
    'task-number-one': {
        'task': 'app1.tasks.task_number_one',
        'schedule': crontab(minute=59, hour=23),
    },
    'task-number-two': {
        'task': 'app2.tasks.task_number_two',
        'schedule': crontab(minute=0, hour='*/3,10-19'),
    }
}