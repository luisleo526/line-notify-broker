from typing import Any

from pydantic import BaseModel, Field


class TextOnly(BaseModel):
    text: str = Field(..., title="Text", description="Text content")


class Token(BaseModel):
    access_token: str = Field(default='example_token')
    token_type: str = Field(default='bearer')


class TradingViewPayload(BaseModel):
    token: str = Field(..., title="Token", description="API token for Line Notify")
    message: Any = Field(..., title="Message", description="Message content")
