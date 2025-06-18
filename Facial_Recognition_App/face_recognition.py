from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #1st image
        img_top=Image.open(r"Facial_Recognition_App\images_face_recog\face_recog1.jpg")
        img_top=img_top.resize((650,700), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place( x = 0,y=55,width=650, height=700)

        #2nd image
        img_bottom=Image.open(r"Facial_Recognition_App\images_face_recog\face_recog2.jpg") 
        img_bottom=img_bottom.resize((950,700), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place( x = 650,y=55,width=950, height=700)

        #button
        b1_1 = Button(f_lbl, text="Face Recognition",cursor = "hand2",  command=self.face_recog,
                         font=("times new roman",18 , "bold"),bg="darkgreen", fg="white",)
        b1_1.place(x=365, y=640,width=200, height=40)
        
    # attendance
    def mark_attendance(self,i,r,n,d):
        with open(r"Facial_Recognition_App\Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and  (n not in name_list) and (r not in name_list) and  (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                 
            
        
        
        
        
        
        
    # face_recognition
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Ritikantjuhi@1234",
                        database="face_recognizer")
                    my_cursor = conn.cursor()

                    # Use parameterized queries for safety
                    my_cursor.execute("SELECT Name FROM user WHERE ID="+ str(id,))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n else ""

                    my_cursor.execute("SELECT roll FROM user WHERE ID=%s", (id,))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r else ""

                    my_cursor.execute("SELECT dep FROM user WHERE ID=%s", (id,))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d else ""
                    
                    my_cursor.execute("SELECT ID FROM user WHERE ID=%s", (id,))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if i else ""

                except Exception as e:
                    print("Database error:", e)
                    n, r, d = "", "", ""
                finally:
                    if 'conn' in locals():
                        conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                 #   cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8, (255, 255, 255), 2)
                coord = [x, y, w, h]
            return coord
    
        def recognize(img, clf, faceCascade):
                coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
                return img

        faceCascade = cv2.CascadeClassifier(r"Facial_Recognition_App\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"Facial_Recognition_App\classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            # Press 'q' to exit
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()  
    app = Face_Recognition(root)
    root.mainloop()  