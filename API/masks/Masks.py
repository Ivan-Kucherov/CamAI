import os
import cv2
import time
from .utils import fps_scale, colorBackgroundText, FONT, read_csv
from fastapi import FastAPI, Request
from .medipipe_masks import mediapipe_main

maskapi = FastAPI()
@maskapi.get('/')
async def start():
    return 'True'
@maskapi.get('/list')
async def list_():
    maskapi.list = [i[:str(i).find('.csv')] for i in os.listdir('./masks/masks/') if str(i).find('.csv') != -1]
    return maskapi.list

@maskapi.get('/set/')
async def set_(num:int=0):
    f = open("mask.txt", "w")
    f.write(str(maskapi.list[num]))
    maskapi.mask = maskapi.list[num]
    f.close()
    return True
cap = cv2.VideoCapture('./test_videos/video_fr11.mp4')

mask_img = cv2.imread('./masks/masks/glasses2.png', cv2.IMREAD_UNCHANGED)
mask_csv = read_csv('./masks/masks/glasses2.csv')


p_time = 0
w, h = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
scale = fps_scale(w, h) 

# video=cv2.VideoWriter('video.avi',-1,24,(w,h))
"""
while True:
    success, img = cap.read()


    if not success:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time


    img = mediapipe_main(img, mask_img, mask_csv, w, h, False)

    colorBackgroundText(img, f"FPS: {int(fps)}", FONT, scale[0], (scale[1],scale[2]), scale[3], (0,255,255), (0,0,0), scale[4], scale[4])

    cv2.imshow('webcam', img)
    #video.write(img)

    #video.release()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#video.release()
cap.release()
"""
cv2.destroyAllWindows()
