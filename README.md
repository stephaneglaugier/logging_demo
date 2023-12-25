# Logging Demo
Simple FastAPI app which logs incoming post requests.

The app returns HTTP code 202 'Accepted' and uses FastAPI's `BackgroundTasks` to asynchronously log the payload to the given file.
```
log_router took 0.000084 seconds to execute.
async_log took 0.003367 seconds to execute.
```
This speeds up performance as well as decoupling response times from the size of the logged payload.

## Setup

Follow these steps to set up the project:

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```

After setting up, you can visit the `/docs` endpoint in your web browser to view the Swagger documentation for the API.

## API Documentation

This application exposes a single API endpoint `/v1/log` which accepts POST requests.

### POST /v1/log

This endpoint is used to log messages. The request body should be a JSON object with the following properties:

- `file_name`: The name of the log file to write to. It should be a string of maximum 20 characters, and should match the pattern `^[a-zA-Z0-9_-]+\\.log$`. For example: `"mylogfile.log"`.
- `level`: The level of the log message. It should be a string that matches the pattern `^(debug|info|warning|error|critical)$`. For example: `"info"`.
- `context`: The context of the log message. It should be a string of maximum 20 characters. For example: `"foo"`.
- `message`: The log message. It should be a string of maximum 1000 characters. For example: `"This is a log message"`.

All properties are required.

The endpoint responds with a status code of 202 if the log message was successfully processed. In case of a validation error, it responds with a status code of 422 and a JSON object describing the validation errors.