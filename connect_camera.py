import cv2

# # Set the serial number of the camera
# serial_number = "2b03:f880"

# # Initialize the VideoCapture object with the serial number
# cap = cv2.VideoCapture(cv2.CAP_DSHOW + 1)
# cap.set(cv2.CAP_PROP_SERIAL_NUMBER, serial_number)

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
