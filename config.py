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
    ASSISTANT_USERNAME = ""
    ASSISTANT_PASSWORD = ""
    ASSISTANT_WORKSPACEID = ""
