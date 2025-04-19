import cv2
import dlib

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Initialize dlib's face detector
detector = dlib.get_frontal_face_detector()

while True:
    # Read the frame
    ret, frame = cap.read()

    if not ret or frame is None:
        print("Failed to grab frame.")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    # Loop through each face detected and draw rectangle
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

    # Show the output
    cv2.imshow("Frame", frame)

    # Exit loop if 'q' is pressed
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
