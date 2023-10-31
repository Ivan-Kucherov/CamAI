import cv2
import numpy as np
import mediapipe as mp
from utils import colorBackgroundText, FONT, read_csv
import time


# Функция определяющая ключевы точки на лице
def landmarks_detection(img, results, draw=False):
    img_height, img_width = img.shape[:2]
    mesh_coord = [(int(point.x * img_width), int(point.y * img_height)) for point in results.multi_face_landmarks[0].landmark]
    landmarks = results.multi_face_landmarks
    if draw:
        [cv2.circle(img, p, 2, (0,255,0), -1) for p in mesh_coord]

    return mesh_coord, landmarks

# Функция для подсчета векторного расстояния
def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


# Функция для движения рта
def lips_ratio(landmarks):
    head_distance = calculate_distance((landmarks[10].x, landmarks[10].y),
                                        (landmarks[152].x, landmarks[152].y)) * 100

    lips_distance = calculate_distance((landmarks[13].x, landmarks[13].y),
                                        (landmarks[14].x, landmarks[14].y)) * 100


    head_lips = lips_distance / head_distance * 100

    if head_lips >= 2:
        print(f'Открытие рта {time.ctime(time.time())}')
        color = [(0,0,0), (0,0,255)]
    else:
        color = [(0,0,0), (0,100,255)]

    return head_lips, color


def warp_image(img, landmarks_coord, w, h, im_src, mask_coord):

    pts_src = np.array(mask_coord, dtype=float)

    pts_dst = np.array(landmarks_coord, dtype=float)
    fh, status = cv2.findHomography(pts_src, pts_dst)
    im_out = cv2.warpPerspective(im_src, fh, (int(w),int(h)))

    
    src = im_out.astype(float)
    src = im_out / 255.0
    alpha_foreground = src[:,:,3]


    dst = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    dst = dst.astype(float)
    dst = dst / 255.0


    for color in range(0, 3):
        dst[:,:,color] = alpha_foreground*src[:,:,color] + (1-alpha_foreground)*dst[:,:,color]

    dst[:,:,:] = cv2.erode(dst[:,:,:],(5,5),0)
    dst[:,:,:] = cv2.GaussianBlur(dst[:,:,:],(3,3),0)

    return dst


def mask_overlay(img, img_landmarks, w, h, mask_img, mask_csv):

    ids, mask_coordinates = mask_csv

    landmarks_coordinates = []
    for landmark_of_interest in ids:
        x = int(img_landmarks[landmark_of_interest].x*w)
        y = int(img_landmarks[landmark_of_interest].y*h)
        landmarks_coordinates.append([x,y])

    
    output = warp_image(img, landmarks_coordinates, w, h, mask_img, mask_coordinates)

    return output




def mediapipe_main(img, mask_img, mask_csv, w, h, draw_all = False):

    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results  = face_mesh.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)



        if results.multi_face_landmarks:
            mesh_coords, landmarks = landmarks_detection(img, results, False)


            landmarks = results.multi_face_landmarks[0].landmark


            # Глаза
            # cv2.polylines(img, [np.array([mesh_coords[p] for p in LEFT_EYE], dtype=np.int32)], True, (0,255,0), 1, cv2.LINE_AA)
            # cv2.polylines(img, [np.array([mesh_coords[p] for p in RIGHT_EYE], dtype=np.int32)], True, (0,255,0), 1, cv2.LINE_AA)


            # Губы
            # pos_lips, color_lips = lips_ratio(landmarks)

            # [cv2.circle(img, mesh_coords[p], 1, (0, 255, 0), -1, cv2.LINE_AA) for p in LIPS]

            # scale_lips = lips_scale(w, h)
    
            # colorBackgroundText(img, f"LIPS: {pos_lips:.3f}", FONT, scale_lips[0], (scale_lips[1], scale_lips[2]), scale_lips[3], color_lips[0], color_lips[1], scale_lips[4], scale_lips[4])


        img = mask_overlay(img, landmarks, w, h, mask_img, mask_csv)


    return img