
import pyautogui
import cv2
import numpy as np
import time

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# Video settings
fps = 10
output_file = "screen_recording.avi"

# Video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Create video writer
out = cv2.VideoWriter(
    output_file,
    fourcc,
    fps,
    (screen_width, screen_height)
)

print("Screen recording will start in 3 seconds...")
time.sleep(3)

print("Recording started. Press Ctrl+C in the terminal to stop.")

try:
    while True:
        # Capture screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to NumPy array
        frame = np.array(screenshot)

        # Convert RGB to BGR for OpenCV
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write frame to video
        out.write(frame)

        # Control recording speed
        time.sleep(1 / fps)

except KeyboardInterrupt:
    print("\nRecording stopped.")

finally:
    out.release()
    cv2.destroyAllWindows()
