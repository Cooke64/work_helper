from __future__ import absolute_import
import os


from celery import Celery, shared_task
from dotenv import load_dotenv


load_dotenv()

broker_url = 'redis://localhost:6379/0'
broker = broker_url if os.environ['DEBUG'] else os.environ['CELERY_BROKER_URL']
app = Celery('celery_app', broker=broker)


@shared_task
def create_report(file_name: str = 'html', type_report: str = 'html') -> int:
    from handlers.admin.report_admin.report_utils import write_file
    try:
        write_file(file_name, type_report)
        return 1
    except Exception as e:
        print(e)
        return 0

# celery -A celery_app beat --loglevel=INFO
# celery -A celery_app worker --loglevel=INFO -P eventlet
