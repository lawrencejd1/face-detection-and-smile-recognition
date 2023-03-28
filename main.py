import cv2

# Load the cascades for face detection and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Start the webcam
cap = cv2.VideoCapture(0)

# Define font and colors for text display
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
fontScale = 1
color_neutral = (255, 255, 255) # white
color_smiling = (0, 255, 0) # green
color_frowning = (0, 0, 255) # red

# Loop through the frames from the webcam
while True:
    # Read the frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Loop through each face and detect smiles
    for (x,y,w,h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Convert the face to grayscale for smile detection
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect smiles in the face image
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        
        # If a smile is detected, print "smiling"
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', org, font, fontScale, color_smiling, 2, cv2.LINE_AA)
        # If no smile is detected, print "neutral"
        else:
            cv2.putText(frame, 'neutral', org, font, fontScale, color_neutral, 2, cv2.LINE_AA)

    # Display the resulting image
    cv2.imshow('Smile Detector', frame)
    
    # Exit the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
