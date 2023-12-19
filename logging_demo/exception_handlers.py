import logging

from fastapi.exception_handlers import (
    HTTPException, JSONResponse, Request, RequestValidationError, Response,
    WebSocket, WebSocketRequestValidationError, http_exception_handler,
    request_validation_exception_handler,
    websocket_request_validation_exception_handler)


async def logged_http_exception_handler(
    request: Request,
    exc: HTTPException
) -> Response:
    logging.error(exc.detail)
    return await http_exception_handler(request, exc)


async def logged_request_validation_exception_handler(
    request: Request,
    exc: RequestValidationError
) -> JSONResponse:
    logging.error(exc.errors())
    return await request_validation_exception_handler(request, exc)


async def logged_websocket_request_validation_exception_handler(
    websocket: WebSocket,
    exc: WebSocketRequestValidationError
) -> None:
    logging.error(exc.errors())
    return await websocket_request_validation_exception_handler(websocket, exc)
