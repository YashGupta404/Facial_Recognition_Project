from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0") 
        
        #title
        title_lbl=Label(self.root, text="Train Dataset", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top=Image.open(r"Facial_Recognition_App\images_face_recog\facialrecognition.png") # JO BHI ISPE KAAM KAR RHA HAI WO EK ACCHA SA IMAGE DALEGA YAHA AUR USKA NAAM facialrecognition.png RAKHNA USS IMAGE KO IMAGES_FACE_RECOG FOLDER MEIN RAKHNA HAI
        #ROHIT TUM HI KARLENA MAI WAISE BATA DIYA HUNGA GRP MAI
        
        
        img_top=img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top=ImageTk. PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place( x = 0,y=55,width=1530, height=325)
        
        #button
        b1_1 = Button(self.root, text="Train Data",command = self.train_classifier,cursor = "hand2",
                         font=("times new roman",30 , "bold"),bg="red", fg="white", command=self.train_classifier)
        b1_1.place(x=0, y=380,width=1530, height=60)
        
        img_bottom=Image.open(r"Facial_Recognition_App\images_face_recog\opencv_face_reco_more_dat.jpg") # Isko bhi ek accha sa image daalna hai jo ki face recognition ke baare mein ho aur uska naam opencv_face_reco_more_dat.jpg rakhna hai images_face_recog folder mein
        #ROHIT TUM HI KARLENA MAI WAISE BATA DIYA HUNGA GRP MAI
        
        
        img_bottom=img_bottom.resize((1530,325), Image.LANCZOS)
        self.photoimg_top=ImageTk. PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place( x = 0,y=440,width=1530, height=325)
        
    def train_classifier(self):
        data_dir = (r"Facial_Recognition_App\data")  # Path to the dataset directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]  # List of all files in the dataset directory
        faces = []  # List to hold the face images
        ids = []  # List to hold the corresponding IDs
        for image in path:
            img = Image.open(image).convert('L')  # Convert the image to grayscale
            imageNp = np.array(img, 'uint8')  # Convert the image to a NumPy array
            id = int(os.path.split(image)[1].split('.')[1])  # Extract the ID from the filename
            faces.append(imageNp)  # Append the image to the faces list
            ids.append(id)  # Append the ID to the ids list
            cv2.imshow("Training", imageNp)  # Display the image (optional)
            cv2.waitKey(1) == 13  # Wait for a key press (optional)
        ids = np.array(ids)  # Convert the ids list to a NumPy array
        
        
        # Train the classifier and save it
        
        clf = cv2.face.LBPHFaceRecognizer_create()  # Create a Local Binary Patterns Histograms (LBPH) face recognizer
        clf.train(faces, ids)  # Train the classifier with the faces and ids
        clf.write("Facial_Recognition_App/classifier.xml")
        cv2.ALLWindows()  # Close all OpenCV windows
        cv2.destroyAllWindows()  # Destroy all OpenCV windows
        messagebox.showinfo("Result", "Training datasets completed successfully")  # Show a message box indicating success

        
            
            
            
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()  