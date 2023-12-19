import logging
import os
from logging.handlers import TimedRotatingFileHandler

from logging_demo.consts import LOGGING_SERVICE_FORMATTER, LOGS_DIR
from logging_demo.decorators import timed_coroutine
from logging_demo.models import LogPayload

loggers: dict[str, logging.Logger] = {}


def get_logger(file_name: str) -> logging.Logger:
    if file_name in loggers:
        return loggers[file_name]
    logger = logging.getLogger(file_name)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    file_handler = TimedRotatingFileHandler(
        os.path.join(LOGS_DIR, file_name),
        when='midnight',
        interval=1,
        backupCount=0
    )
    file_handler.suffix = '%Y-%m-%d.log'
    file_handler.setFormatter(LOGGING_SERVICE_FORMATTER)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    loggers[file_name] = logger
    return logger


@timed_coroutine
async def async_log(payload: LogPayload):
    logger = get_logger(payload.file_name)
    log_func = getattr(logger, payload.level)
    log_func(payload.message, extra={"context": payload.context})
