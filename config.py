DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"

SECRET_KEY = "secret"

class dev_config():
    ASSISTANT_VERSION = "2018-02-16"
    ASSISTANT_USERNAME = "2f27a362-a5da-4f9a-9877-7fdfb77b7942"
    ASSISTANT_PASSWORD = "22jeKRq4lkV1"
    ASSISTANT_WORKSPACEID = "66a052f0-cc1b-492b-9b05-4a84b0b10fc8"