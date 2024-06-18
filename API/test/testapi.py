# fastapi_app.py

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from camera_single import Camera
from .camera_multi import Camera

testapp = FastAPI()
testapp.test = "00"
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@testapp.get("/", response_class=HTMLResponse)
async def index(request: Request):
   return templates.TemplateResponse('index.html', {"request": request})

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@testapp.get('/video_feed', response_class=HTMLResponse)
async def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return  StreamingResponse(gen(Camera()),
                    media_type='multipart/x-mixed-replace; boundary=frame')
@testapp.get('/')
async def api():
    return "True"
