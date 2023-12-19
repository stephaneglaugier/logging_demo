import os
from logging import Formatter

DEFAULT_FORMATTER = Formatter(
    "%(asctime)s|%(levelname)s|%(thread)s|%(name)s|%(message)s"
)

LOGGING_SERVICE_FORMATTER = Formatter(
    "%(asctime)s|%(levelname)s|%(thread)s|%(context)s|%(message)s"
)

LOGS_DIR = "logs/"

SVC_LOG_FILE = "logging_demo.log"

SVC_LOG_DIR = os.path.join(LOGS_DIR, SVC_LOG_FILE)
