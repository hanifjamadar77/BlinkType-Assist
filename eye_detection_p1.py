import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:\pthon\BlinkType Assist\shape.dat\shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        # x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        # left_point = (landmarks.part(36).x, landmarks.part(36).y)
        # right_point = (landmarks.part(39).x, landmarks.part(39).y)
        # center_top = midpoint(landmarks.part(37), landmarks.part(38))
        # center_bottom = midpoint(landmarks.part(41), landmarks.part(40))

        # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
        # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),(landmarks.part(37).x, landmarks.part(37).y),(landmarks.part(38).x, landmarks.part(38).y),(landmarks.part(39).x, landmarks.part(39).y),(landmarks.part(40).x, landmarks.part(40).y),(landmarks.part(41).x, landmarks.part(41).y)],np.int32)
        cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

        # cv2.polylines(frame, landmarks, True, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()