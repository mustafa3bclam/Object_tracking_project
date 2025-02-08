import cv2
import numpy as np
import streamlit as st # type: ignore
import cv2
import numpy as np
import tempfile
import time


capturtes = cv2.VideoCapture(r"C:\Users\LENOVO\Downloads\Route\background video _ people _ walking _.mp4")
back_sub = cv2.createBackgroundSubtractorMOG2()

while capturtes.isOpened():
    ret, frame = capturtes.read() 
    if not ret:
        break
    fg_mask = back_sub.apply(frame)
    (contours , _ )=cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        if cv2.contourArea(i) > 500:
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow("foreground mask", fg_mask)
    cv2.imshow("original feed", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break
    
capturtes.release()
cv2.destroyAllWindows()


def convert_color(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

st.title("Object Detection")

upload = st.file_uploader("Choose a Video...", type=["MP4", "MOV", "AVI"])

if upload is not None:
    #Save video in temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(upload.read())
    tfile.close()
    
    capturtes = cv2.VideoCapture(tfile.name)
    if not capturtes.isOpened():
        st.write("Error: Video file not found")
    
    else:
        stframe = st.empty()#Placeholder for video frame
        back_sub = cv2.createBackgroundSubtractorMOG2()
        while capturtes.isOpened():
            ret, frame = capturtes.read() 
            if not ret:
                break
            fg_mask = back_sub.apply(frame)
            (contours , _ )=cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for i in contours:
                if cv2.contourArea(i) > 500:
                    x,y,w,h = cv2.boundingRect(i)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            stframe.image(convert_color(frame)) #Display video frame
            time.sleep(0.003)
        capturtes.release()
else:
    st.warning("please upload a video")