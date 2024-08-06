import json

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from src.schemas.basic import TextOnly, TradingViewPayload

LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"
app = FastAPI(
    title="A Line Notify API Broker",
    description="Receive a request from a client and send a message to Line Notify",
    version="0.0.1",
    contact={
        "name": "Hao-Liang Wen",
        "email": "luisleo52655@gmail.com",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.post("/")
async def send_line_notify(
        payload: TradingViewPayload
):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + payload.token
    }

    payload = 'message=' + json.dumps(payload.message, ensure_ascii=False, indent=2)

    response = requests.post(
        LINE_NOTIFY_URL,
        headers=headers,
        data=payload
    )

    return response.json()


@app.get("/", response_model=TextOnly)
async def root():
    return TextOnly(text="Hello World")


@app.get("/elements", include_in_schema=False)
async def api_documentation(request: Request):
    return HTMLResponse("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Elements in HTML</title>

    <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
  </head>
  <body>

    <elements-api
      apiDescriptionUrl="openapi.json"
      router="hash"
    />

  </body>
</html>""")
