import cv2
import os
import pickle
import numpy as np

# Directory to save face data
if not os.path.exists('data/'):
    os.makedirs('data/')

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Collect face data
def collect_faces():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    video = cv2.VideoCapture(0)
    collected_faces = []
    count = 0

    try:
        while True:
            ret, frame = video.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facedetect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                face = gray[y:y + h, x:x + w]
                face = cv2.resize(face, (50, 50))  # Resize to a fixed size
                collected_faces.append(face.flatten())  # Flatten to 1D array

                # Draw rectangle around detected face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1

            # Show live video feed
            cv2.imshow("Collecting Faces", frame)

            # Break loop after collecting 100 images or on pressing 'q'
            if count >= 100 or cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video.release()
        cv2.destroyAllWindows()

    if collected_faces:
        # Save collected data
        with open('data/name.pkl', 'ab') as f:
            labels = [name] * len(collected_faces)
            pickle.dump(labels, f)

        with open('data/faces.pkl', 'ab') as f:
            pickle.dump(collected_faces, f)

        print(f"Collected {len(collected_faces)} images for {name}.")
    else:
        print("No faces collected.")

# Run the face collection process
if __name__ == "__main__":
    collect_faces()
