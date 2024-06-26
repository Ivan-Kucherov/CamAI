# fastapi_app.py

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#Simple page for camera testing(if you have camera)
from test import testapi
#api for changing masks
from masks import Masks

app = FastAPI()
@app.get('/')
async def api():
    return "True"
app.mount('/test',testapi)

app.mount('/mask',Masks.maskapi)

if __name__ == "__main__":
    print('stop: ctrl+c')
    uvicorn.run(app, host="192.168.1.6", port=8000,log_level="info")
    from fastapi import FastAPI

#app.mount("/static", StaticFiles(directory="static"), name="static")
