from pydantic import BaseModel, Field, validator

from logging_demo.consts import SVC_LOG_FILE


class LogPayload(BaseModel):
    file_name: str = Field(
        ...,
        max_length=20,
        description="The name of the log file to write to",
        example="mylogfile.log",
        pattern="^[a-zA-Z0-9_-]+\.log$"  # noqa: W605
    )
    level: str = Field(
        ...,
        description="The level of the log message",
        example="info",
        pattern="^(debug|info|warning|error|critical)$",
    )
    context: str = Field(
        ...,
        max_length=20,
        example="foo"
    )
    message: str = Field(
        ...,
        max_length=1000,
        example="This is a log message"
    )

    @validator('file_name')
    def validate_file_name(cls, file_name):
        protected_values = [SVC_LOG_FILE]
        if file_name in protected_values:
            raise ValueError(f"file_name cannot be equal to '{file_name}'")
        return file_name
