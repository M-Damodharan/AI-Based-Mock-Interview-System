import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    ###DF
    try:
        results = DeepFace.analyze(img_path=image, actions=['emotion'], enforce_detection=True)
        if isinstance(results, list):  
            results = results[0]
        dominant_emotion = results.get('dominant_emotion', 'Unknown')
        
        #result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        ########
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw the rectangle around each face
        j = 1
        for (x, y, w, h) in faces:
            #mm=cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

            thickness = 2
            fontSize = 0.5
            step = 20
            #txt = str(result[0]['dominant_emotion'])
            txt=dominant_emotion
            emotion2="Emotion: "+txt
            cv2.putText(image, emotion2, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
            
            j += 1

            emo=emotion2+","
            ff1=open("emotion.txt","a")
            ff1.write(emo)
            ff1.close()

            

    except Exception as e:
            print("Error:", e)       
    #demography = DeepFace.analyze("juan.jpg", actions = ['age', 'gender', 'race', 'emotion'])

    #result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)
    
    #result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)
    '''gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        #emotionz = result["dominant_emotion"]
        #txt = str(result['dominant_emotion'])
        txt = str(result[0]['dominant_emotion'])
        #txt2 = str(result[0]['age'])
        #txt3 = str(result[0]['gender'])

        thickness = 1
        fontSize = 0.5
        step = 13

        cv2.putText(frame, txt, (x, y-12),cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
        #cv2.putText(frame, txt2, (x, y-step-10*1), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
        #cv2.putText(frame, txt3, (x, y-step-10*2), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
        #cv2.putText(frame, txt, (x, y+3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        #cv2.putText(frame, txt2, (x, y+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        #cv2.putText(frame, txt3, (x, y+9), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)'''
    cv2.imshow('frame', image)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
