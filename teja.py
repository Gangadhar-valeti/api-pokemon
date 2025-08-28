import cv2
import dlib
import numpy as np

def midpoint(p1, p2):
    return (p1.x + p2.x) // 2, (p1.y + p2.y) // 2

# Calculate Eye Aspect Ratio (EAR) to detect blinking
def calculate_ear(eye_points, landmarks):
    A = np.linalg.norm(np.array([landmarks.part(eye_points[1]).x, landmarks.part(eye_points[1]).y]) - 
                       np.array([landmarks.part(eye_points[5]).x, landmarks.part(eye_points[5]).y]))
    B = np.linalg.norm(np.array([landmarks.part(eye_points[2]).x, landmarks.part(eye_points[2]).y]) - 
                       np.array([landmarks.part(eye_points[4]).x, landmarks.part(eye_points[4]).y]))
    C = np.linalg.norm(np.array([landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y]) - 
                       np.array([landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y]))

    ear = (A + B) / (2.0 * C)
    return ear

# Detect pupil position with bounding box
def get_pupil_position(eye_points, landmarks, frame):
    left_x = landmarks.part(eye_points[0]).x
    right_x = landmarks.part(eye_points[3]).x
    top_y = min(landmarks.part(eye_points[1]).y, landmarks.part(eye_points[2]).y)
    bottom_y = max(landmarks.part(eye_points[4]).y, landmarks.part(eye_points[5]).y)

    eye_region = frame[top_y:bottom_y, left_x:right_x]
    gray_eye = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding
    threshold_eye = cv2.adaptiveThreshold(gray_eye, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    contours, _ = cv2.findContours(threshold_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)  # Bounding box coordinates
        
        # Draw square box around pupil
        cv2.rectangle(frame, (left_x + x, top_y + y), (left_x + x + w, top_y + y + h), (0, 255, 0), 2)

        pupil_x = x + w // 2  # Center of the bounding box
        eye_width = right_x - left_x

        if pupil_x < eye_width * 0.35:
            return "LEFT"
        elif pupil_x > eye_width * 0.65:
            return "RIGHT"
        else:
            return "FORWARD"

    return "FORWARD"

# Initialize dlib face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Camera not detected!")
    exit()

EAR_THRESHOLD = 0.2
BLINK_FRAMES = 5
blink_counter = 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = cv2.flip(frame, 1)  # Flip for correct left-right tracking

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        if len(faces) == 0:
            cv2.putText(frame, "No Face Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        for face in faces:
            landmarks = predictor(gray, face)

            left_eye_ear = calculate_ear([36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ear = calculate_ear([42, 43, 44, 45, 46, 47], landmarks)
            avg_ear = (left_eye_ear + right_eye_ear) / 2.0

            if avg_ear < EAR_THRESHOLD:  # If eyes are closed, set STOP and skip pupil detection
                blink_counter += 1
                if blink_counter >= BLINK_FRAMES:
                    gaze_direction = "STOP"
            else:
                blink_counter = 0
                gaze_direction = get_pupil_position([36, 37, 38, 39, 40, 41], landmarks, frame)

            cv2.putText(frame, f"Gaze: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Eye Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released. Windows closed.")