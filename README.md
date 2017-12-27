### Flask Celery Demo

* Python3
* Flask
* Celery
* Blueprint

#### Quick Setup

1. Clone this repository.
2. Create virtualenv (1. `mkdir flaskdemo`  2. `pyvenv venv`  3. `source venv/bin/active`)
3. Install requirements (`pip install requirements.txt`)
4. Set Celery broker_url of Redis in `jobs/celeryconfig.py`
5. Set two environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` to 163.com . Set environment variables:   
```
export MAIL_USERNAME='your_163_email_addr'
export MAIL_PASSWORD='your_163_email_pwd'
```
(this demo use 163.com,use other email SMTP server by yourself configued in `config.py`)
6. Open a terminal window run flask web(`python run.py`)
7. Open a second terminal window start a Celery worker (`celery worker -A celery_worker.celery -l=info`)
8. Open a third terminal window start a Celery worker (`celery beat -A celery_worker.celery -l=info`)
9. Or Run (`celery worker -B -A celery_worker.celery -l=info`) instead of step 7 and step 8
10. Go to `http://localhost:5000/` test.
11. Enjoy it.






