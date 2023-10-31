import cv2
import time
from utils import fps_scale, colorBackgroundText, FONT, read_csv
from medipipe_masks import mediapipe_main

def main():
    cap = cv2.VideoCapture('D:/machine_learning1/CamAI/test_videos/video_fr11.mp4')

    mask_img = cv2.imread('D:/machine_learning1/CamAI/masks/glasses2.png', cv2.IMREAD_UNCHANGED)
    mask_csv = read_csv('D:/machine_learning1/CamAI/masks/11112.csv')


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