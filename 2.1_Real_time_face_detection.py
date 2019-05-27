# import the libraries
import os
import cv2
import face_recognition

#loading video
cap = cv2.VideoCapture(0)

#load image to be matched
match_face = face_recognition.load_image_file('1.jpg')
name_face = str(input("Enter name of the face to be matched: "))

# encoded the loaded image into a feature vector
match_face_encoded = face_recognition.face_encodings(
    match_face)[0]

# iterate over each image
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    #initiating variables
    face_locations = []
    face_encodings = []
    frame_process = True
    face_names = []

    if frame_process:

        #fetching a list of faces in the frame
        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) == 0:
            print("No Face in the frame")

        else:
            current_frame_encoded = face_recognition.face_encodings(frame, face_locations)

            for face_encoded in current_frame_encoded:

                # check if the current face matches with the face to be matched
                result = face_recognition.compare_faces([match_face_encoded], face_encoded)
                if result[0] == True:
                    print("Matched")
                    status = "matched"
                else:
                    print("Face not matched")
                    status = "not matched"

    frame_process = not frame_process

    #displaying result
    for (top, right, bottom, left) in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        if status == "matched":
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name_face, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        else:
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Unknown", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    
