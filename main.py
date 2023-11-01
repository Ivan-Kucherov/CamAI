import cv2
import time
from utils import fps_scale, colorBackgroundText, FONT, read_csv
from medipipe_masks import mediapipe_main
import pandas as pd

def main():
    cap = cv2.VideoCapture('test_videos/video_fr11.mp4')
    name_mask = "batman_1"
    mask_img = cv2.imread(f'masks/{name_mask}.png', cv2.IMREAD_UNCHANGED)
    mask_csv = read_csv(f'masks/{name_mask}.csv')
    #Альфа канал
    if mask_img.shape[2] == 3:
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2BGRA)

    p_time = 0
    w, h = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    scale = fps_scale(w, h) 

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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
