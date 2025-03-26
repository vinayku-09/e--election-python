# Smart Election System

## Overview
The **Smart Election System** is a secure and automated e-voting system that leverages facial recognition technology to ensure voter authentication and prevent duplicate votes. This system allows voters to cast their votes in a user-friendly GUI and records votes securely in a CSV file.

## Features
- **Face Recognition-based Voter Authentication**: Ensures only registered users can vote.
- **Graphical User Interface (GUI)**: Provides an easy-to-use interface for casting votes.
- **Secure Vote Recording**: Stores votes with voter ID, selected party, and timestamp.
- **Automated Voice Alerts**: Provides real-time feedback using Text-to-Speech (TTS).
- **Real-time Video Capture**: Displays a live video feed to confirm voter presence.

## Project Structure
```
SmartElectionSystem/
│── data/                 # Directory for storing face data
│── images/               # Directory for storing party logos
│── collect_faces.py      # Script to collect and store voter face data
│── give_vote.py          # Main voting system script with GUI
│── requirement.txt       # Dependencies required to run the project
│── votes.csv             # File for storing recorded votes
```

## Installation
### Prerequisites
- Python 3.x
- Webcam for face recognition
- Windows OS (TTS feature requires `pywin32`)

### Step 1: Install Dependencies
Run the following command to install the required packages:
```bash
pip install -r requirement.txt
```

### Step 2: Run Face Collection Script
Before voting, users need to register their faces:
```bash
python collect_faces.py
```
This will prompt users to enter their name and capture 100 face images.

### Step 3: Run the Voting System
Once registered, users can cast their votes:
```bash
python give_vote.py
```

## How It Works
1. **Face Data Collection (`collect_faces.py`)**
   - Detects and captures face images.
   - Stores face data as `.pkl` files.
   - Uses OpenCV’s Haar Cascade Classifier for face detection.

2. **Voting Process (`give_vote.py`)**
   - Displays a live video feed in the GUI.
   - Allows users to select their preferred party using buttons.
   - Records vote details in `votes.csv`.
   - Uses TTS to confirm vote submission.

## Technologies Used
- **Python** (Core programming language)
- **OpenCV** (Face detection and video capture)
- **Tkinter** (GUI development)
- **PIL (Pillow)** (Image processing)
- **pywin32** (Text-to-Speech on Windows)

## Future Enhancements
- **Integrate with Blockchain** for immutable vote storage.
- **Implement Biometric Verification** for added security.
- **Deploy as a Web-Based Application** for remote voting.

## Contributors
- **Vinay Kumar Singh** and team

## License
This project is for educational purposes only. Modify and use at your own discretion.

# e--election-python
Smart Election System uses face recognition for secure e-voting, preventing duplicate votes. It features real-time authentication, a user-friendly GUI, and secure vote recording with TTS feedback. Built with Python and OpenCV, it ensures a fair and efficient voting process.
