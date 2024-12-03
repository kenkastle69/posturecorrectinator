# Posture Assessment Using MediaPipe and OpenCV

This project assesses the posture of a person by detecting and analyzing key body points using MediaPipe Pose and OpenCV. It calculates the angle between the shoulders, neck, and other body landmarks to provide feedback on whether the posture is good or needs adjustment.

## Features
- Real-time posture assessment using a webcam.
- Calculates the neck angle to determine posture quality.
- Provides feedback on whether the posture is good or needs improvement.
- Visualizes body landmarks and pose connections on the video frame.

## Technologies Used
- **Python**: Programming language used for implementation.
- **OpenCV**: Library used for video capture, image manipulation, and real-time display.
- **MediaPipe**: Used to detect human pose landmarks.
- **NumPy**: For mathematical operations such as angle calculations.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/posture-assessment.git
cd posture-assessment
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
```
3. Install the required libraries
```bash
pip install opencv-python mediapipe numpy
```
Usage
Connect a webcam to your computer.
Run the script:
``` bash
python posture_assessment.py
```
The program will display a real-time video feed from the webcam with the detected body landmarks.
Based on the angle calculated between the shoulders and neck, it will display a message indicating whether the posture is good or requires adjustment.
Key Posture Assessment
If the neck angle is less than 20 degrees, the posture is considered good.
If the neck angle is greater than 20 degrees, the user is encouraged to adjust their posture.
Press 'q' to exit the program.

Example Output
When the script runs, you should see something like this:

Good posture: A green text Posture: Good appears on the screen.
Adjust your posture: A red text Posture: Adjust your back appears if the posture needs improvement.
Contributing
Feel free to fork this repository, submit issues, and create pull requests.

Steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
MediaPipe for providing an easy-to-use pose estimation solution.
OpenCV for video capture and manipulation.
