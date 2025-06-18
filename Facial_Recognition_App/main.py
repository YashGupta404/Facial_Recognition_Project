from tkinter import* # Importing the tkinter library for GUI applications
from tkinter import ttk # used for themed widgets
from PIL import Image, ImageTk # Importing pillow for image handling
from user import User 
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance_management

class face_recognition:
    # Constructor to initialize the main window
    def __init__(self, root): 
        self.root = root # Initializing the main window
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0") # Setting the size and position of the window ie width and height and x and y coordinates
       
       
       #background image
        bg_img = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg") 
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img) 
        self.lbl_bg = Label(self.root, image= self.photobg_img)
        self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
        #logo image
        image = Image.open(r"Facial_Recognition_App\images_face_recog\face-recognition.png") # Opening the image file from the specified path
        # Resizing the image to fit the window and ANTIALIAS is used to convert the image to a lower resolution
        image = image.resize((100, 100), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image) # Converting the image to PhotoImage format for tkinter
        #setting the img to the label to display it in the window
        self.lbl_image = Label(self.root, image= self.photoimage)
        self.lbl_image.place(x=1420, y=10, width=100, height=100)
        
        #title label
        title_lbl = Label(self.root,text="NeuroNest FACECOM",font=("times new roman",35 , "bold"))
        title_lbl.place(x=515, y=50, width=500, height=45)
        #user details
        
        user_img = Image.open(r"Facial_Recognition_App\images_face_recog\list.png") 
        user_img = user_img.resize((180, 180), Image.LANCZOS)
        self.photouser_img= ImageTk.PhotoImage(user_img) 
        user_btn = Button(self.root, image=self.photouser_img,command=self.user_details,cursor = "hand2",)
        user_btn.place(x=200, y=150,width=180, height=180)
        
        user_btn_txt = Button(self.root, text="User Detail",command=self.user_details ,cursor = "hand2",
                         font=("times new roman",12 , "bold"))
        user_btn_txt.place(x=200, y=330,width=180, height=30)
        
        
        #Gender Recognition button
        Gen_img = Image.open(r"Facial_Recognition_App\images_face_recog\atoms.png") 
        Gen_img = Gen_img.resize((180, 180), Image.LANCZOS)
        self.photoGen_img= ImageTk.PhotoImage(Gen_img) 
        Gen_btn = Button(self.root, image=self.photoGen_img, cursor = "hand2",
                        )
        Gen_btn.place(x=700, y=150,width=180, height=180)
        
        Gen_btn_txt = Button(self.root, text="Gender Classification", cursor = "hand2",
                         font=("times new roman",12 , "bold"))
        Gen_btn_txt.place(x=700, y=330,width=180, height=30)
        
        #face detection button
        face_img = Image.open(r"Facial_Recognition_App\images_face_recog\face-detection (1).png") 
        face_img = face_img.resize((180, 180), Image.LANCZOS)
        self.photoface_img= ImageTk.PhotoImage(face_img) 
        face_btn = Button(self.root, image=self.photoface_img, cursor = "hand2", command=self.face_data
                        )
        face_btn.place(x=450, y=150,width=180, height=180)
        
        face_btn_txt = Button(self.root, text="Face Recognition", cursor = "hand2", command=self.face_data,
                         font=("times new roman",12 , "bold"))
        face_btn_txt.place(x=450, y=330,width=180, height=30)
        
          # training button
        
        train_img = Image.open(r"Facial_Recognition_App\images_face_recog\data-warehouse.png") 
        train_img = train_img.resize((180, 180), Image.LANCZOS)
        self.phototrain_img= ImageTk.PhotoImage(train_img) 
        train_btn = Button(self.root, image=self.phototrain_img, cursor = "hand2",command=self.train_data,)
        train_btn.place(x=950, y=150,width=180, height=180)
        
        train_btn_txt = Button(self.root, text="Train Data", cursor = "hand2",command=self.train_data,
                         font=("times new roman",12 , "bold"))
        train_btn_txt.place(x=950, y=330,width=180, height=30)
        
          # Attendance button
        
        att_img = Image.open(r"Facial_Recognition_App\images_face_recog\data-warehouse.png") 
        att_img = att_img.resize((180, 180), Image.LANCZOS)
        self.photoatt_img= ImageTk.PhotoImage(att_img) 
        att_btn = Button(self.root, image=self.photoatt_img, cursor = "hand2",command=self.attend_data,)
        att_btn.place(x=950, y=150,width=180, height=180)
        
        att_btn_txt = Button(self.root, text="Attendance", cursor = "hand2",command=self.attend_data,
                         font=("times new roman",12 , "bold"))
        att_btn_txt.place(x=950, y=330,width=180, height=30)
        
        
        
        #Team
        Team_img = Image.open(r"Facial_Recognition_App\images_face_recog\united.png") 
        Team_img = Team_img.resize((180, 180), Image.LANCZOS)
        self.photoTeam_img= ImageTk.PhotoImage(Team_img) 
        Team_btn = Button(self.root, image=self.photoTeam_img, cursor = "hand2",
                        )
        Team_btn.place(x=700, y=420,width=180, height=180)
        
        Team_btn_txt = Button(self.root, text="Team", cursor = "hand2",
                         font=("times new roman",12 , "bold"))
        Team_btn_txt.place(x=700, y=600,width=180, height=30)
        
        #Help Desk
        help_img = Image.open(r"Facial_Recognition_App\images_face_recog\customer-service.png") 
        help_img = help_img.resize((180, 180), Image.LANCZOS)
        self.photohelp_img= ImageTk.PhotoImage(help_img) 
        help_btn = Button(self.root, image=self.photohelp_img, cursor = "hand2",
                        )
        help_btn.place(x=450, y=420,width=180, height=180)
        
        help_btn_txt = Button(self.root, text="Help Desk", cursor = "hand2",
                         font=("times new roman",12 , "bold"))
        help_btn_txt.place(x=450, y=600,width=180, height=30)
        
        
         
        #photos face button
        photo_img = Image.open(r"Facial_Recognition_App\images_face_recog\customer-service.png") 
        photo_img=photo_img.resize((180, 180), Image.LANCZOS)
        self.photophoto_img= ImageTk.PhotoImage(photo_img) 
        photo_btn = Button(self.root, image=self.photophoto_img, cursor = "hand2",command = self.open_img
                        )
        photo_btn.place(x=200, y=420,width=180, height=180)
        
        photo_btn_txt = Button(self.root, text="Photos", cursor = "hand2", command = self.open_img,
                         font=("times new roman",12 , "bold"))
        photo_btn_txt.place(x=200, y=600,width=180, height=30)
        
    def open_img(self):
      os.startfile(r"Facial_Recognition_App\data")    
        # function for linking the buttons to their respective functionalities
    def user_details(self):
      self.new_window = Toplevel(self.root)
      self.new_obj = User(self.new_window)
    
    def train_data(self):
      self.new_window = Toplevel(self.root)
      self.app = Train(self.new_window)

    def face_data(self):
      self.new_window = Toplevel(self.root)
      self.app = Face_Recognition(self.new_window)  
    
    def attend_data(self):
      self.new_window = Toplevel(self.root)
      self.app = Attendance_management(self.new_window) 
      
        

if __name__ == "__main__":
    # Create the main window
    root = Tk()
    # Create an instance of the face_recognition class
    app = face_recognition(root)
    # Start the main event loop
    root.mainloop()
