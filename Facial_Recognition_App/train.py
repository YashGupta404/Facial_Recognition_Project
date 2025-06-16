from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2


class Train:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0") 
        
        #title
        title_lbl=Label(self.root, text="User detail", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()  