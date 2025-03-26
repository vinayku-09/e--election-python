import cv2
from tkinter import Tk, Label, Button, Frame, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os
from win32com.client import Dispatch

# Function to speak a message using TTS
def speak(message):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(message)

# Function to handle vote registration
def register_vote(party_name):
    global voter_data, voter_id
    # Check if the voter has already voted
    if voter_id in voter_data:
        message = "You have already cast your vote!"
        speak(message)  # Speak the message
        messagebox.showinfo("Already Voted", message)
    else:
        # Record the vote with date and time
        voter_data[voter_id] = party_name
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time
        with open("votes.csv", "a") as file:
            file.write(f"{voter_id},{party_name},{current_time}\n")
        message = f"Your vote for {party_name} has been registered!"
        speak(message)  # Speak the message
        messagebox.showinfo("Vote Registered", message)
        root.destroy()  # Automatically close the application

# Function to add party buttons
def add_party_button(party_name, image_path, row, col):
    try:
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
        img = ImageTk.PhotoImage(img)

        button = Button(party_frame, image=img, text=party_name, compound="top", font=("Arial", 12),
                        command=lambda: register_vote(party_name))
        button.image = img  # Prevent garbage collection of the image
        button.grid(row=row, column=col, padx=10, pady=10)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Image not found: {image_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to show the video feed in the GUI
def show_video():
    _, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (400, 300))
    img = ImageTk.PhotoImage(Image.fromarray(frame))
    video_label.imgtk = img
    video_label.configure(image=img)
    video_label.after(10, show_video)

# Main GUI function
def create_gui():
    global party_frame, video_label

    # Create the main window
    root = Tk()
    root.title("Smart Election Voting System")
    root.geometry("800x600")

    # Title Label
    Label(root, text="Smart Election Voting System", font=("Arial", 24), pady=10).pack()

    # Video Frame
    video_frame = Frame(root)
    video_frame.pack(pady=10)
    global video_label
    video_label = Label(video_frame)
    video_label.pack()

    # Party Buttons Frame
    global party_frame
    party_frame = Frame(root)
    party_frame.pack(pady=10)

    # Add Party Buttons
    add_party_button("BJP", "images/party_a.png", 0, 0)
    add_party_button("Congress", "images/party_b.png", 0, 1)
    add_party_button("Independent", "images/party_c.png", 0, 2)

    # Start Video Feed
    show_video()

    # Run the GUI event loop
    root.mainloop()

# Initialize video capture
video = cv2.VideoCapture(0)

# Ensure the votes file exists
if not os.path.exists("votes.csv"):
    with open("votes.csv", "w") as file:
        file.write("VoterID,Party,DateTime\n")

# Simulated voter data for demonstration (Replace with actual voter identification logic)
voter_id = "VOTER12345"  # This should be dynamically fetched (e.g., via face recognition)
voter_data = {}  # Dictionary to store voter information

# Start the GUI
create_gui()

# Release the video capture when the GUI is closed
video.release()
cv2.destroyAllWindows()
