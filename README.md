### flask_celery_demo

Flask + Celery + Blueprint Demo



export MAIL_USERNAME='your_163_email_addr'
export MAIL_PASSWORD='your_163_email_pwd'


python run.py


celery worker -A celery_worker.celery -l=info


celery beat -A celery_worker.cery -l=info

