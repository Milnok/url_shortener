from config.celery import app
from datetime import datetime, timedelta
from api.models import Url


@app.task
def delete_old_urls():
    last_month = datetime.today() - timedelta(days=30)
    Url.objects.exclude(last_redirect__gt=last_month).delete()
