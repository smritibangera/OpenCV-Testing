import cv2

# Open default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Camera started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcam', gray)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()