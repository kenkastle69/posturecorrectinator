import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize OpenCV for video capture
cap = cv2.VideoCapture(0)


# Function to calculate the angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)  # First point
    b = np.array(b)  # Middle point
    c = np.array(c)  # Last point

    # Calculate the angle
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # Adjust angle to be between 0 and 180
    if angle > 180.0:
        angle = 360 - angle

    return angle


# Function to assess posture
def assess_posture(landmarks):
    # Get the coordinates of relevant body parts (e.g., shoulders, elbows, and hips)
    shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y]
    shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]
    hip_left = [landmarks[mp_pose.PoseLandmark.LEFT_HIP].x,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP].y]
    hip_right = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x,
                 landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y]
    nose = [landmarks[mp_pose.PoseLandmark.NOSE].x,
            landmarks[mp_pose.PoseLandmark.NOSE].y]

    # Calculate angles to assess posture
    # Example: Calculate the angle of the neck (between shoulders and nose)
    neck_angle = calculate_angle(shoulder_left, nose, shoulder_right)

    return neck_angle


# Start video capture
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get the landmarks
    results = pose.process(rgb_frame)

    # Draw the pose landmarks and analyze posture
    if results.pose_landmarks:
        # Draw landmarks
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Assess the posture based on key body points
        neck_angle = assess_posture(results.pose_landmarks.landmark)

        # Display posture feedback
        if neck_angle < 20:
            cv2.putText(frame, "Posture: Good", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Posture: Adjust your back", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Posture Assessment", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()

