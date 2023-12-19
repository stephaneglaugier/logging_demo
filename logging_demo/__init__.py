import logging
import logging.handlers
import os

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import (RequestValidationError,
                                WebSocketRequestValidationError)

from logging_demo.consts import DEFAULT_FORMATTER, LOGS_DIR, SVC_LOG_DIR
from logging_demo.exception_handlers import (
    logged_http_exception_handler, logged_request_validation_exception_handler,
    logged_websocket_request_validation_exception_handler)
from logging_demo.routers import prefix, router


def create_logs_dir_if_not_exists():
    os.makedirs(LOGS_DIR, exist_ok=True)


def configure_root_logger():
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    fh = logging.FileHandler(SVC_LOG_DIR)
    fh.setLevel(logging.INFO)
    for h in [sh, fh]:
        h.setFormatter(DEFAULT_FORMATTER)
        root_logger.addHandler(h)


def create_app():
    app = FastAPI(
        on_startup=[
            create_logs_dir_if_not_exists,
            configure_root_logger,
        ]
    )

    # Routers
    app.include_router(
        router=router,
        prefix=prefix
    )

    # Exception Handlers
    app.add_exception_handler(
        RequestValidationError,
        logged_request_validation_exception_handler
    )
    app.add_exception_handler(
        HTTPException,
        logged_http_exception_handler
    )
    app.add_exception_handler(
        WebSocketRequestValidationError,
        logged_websocket_request_validation_exception_handler
    )

    return app
