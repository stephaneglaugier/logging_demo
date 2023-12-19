import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException, status

from logging_demo.decorators import timed
from logging_demo.models import LogPayload
from logging_demo.services import async_log

router = APIRouter()
prefix = "/v1"


@router.post("/log", status_code=status.HTTP_202_ACCEPTED)
@timed
def log_router(
    payload: LogPayload,
    background_tasks: BackgroundTasks
):
    try:
        background_tasks.add_task(async_log, payload)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail=str(e))
