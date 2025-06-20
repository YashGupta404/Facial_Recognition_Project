from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
import webbrowser # Import webbrowser for clickable email links

class Help:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Help Desk") 
        self.root.geometry("1530x790+0+0") 
        self.root.configure(bg="#ffffff")  # Set window background to white
        
        # Remove/comment out the background image for a plain white background
        # bg_img = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg") 
        # bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        # self.photobg_img = ImageTk.PhotoImage(bg_img) 
        # self.lbl_bg = Label(self.root, image= self.photobg_img)
        # self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
        title_lbl = Label(self.root, text="How can I help you?", font=("times new roman", 30, "bold"), bg="#ffffff", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        cnt_lbl = Label(self.root, text="Contact us", font=("times new roman", 30, "bold"), fg="black", bg="#ffffff")
        cnt_lbl.place(x=70, y=60)

        # Clickable email
        def open_email(event):
            webbrowser.open("mailto:kantjuhi04@gmail.com")

        email_lbl = Label(self.root, text="Email: kantjuhi04@gmail.com", 
                          font=("times new roman", 18, "underline"), fg="blue", cursor="hand2", justify="left", bg="#ffffff")
        email_lbl.place(x=90, y=110)
        email_lbl.bind("<Button-1>", open_email)

        # FAQ Section Title (right side)
        faq_frame_x = 900
        faq_title = Label(self.root, text="Frequently Asked Questions", font=("times new roman", 24, "bold"), fg="#0a4d8c", bg="#ffffff")
        faq_title.place(x=faq_frame_x, y=60)

               # FAQ Content (right side, below FAQ title)
        faq_text = (
            "Q1: How do I register my face?\n"
            "A1: Go to the User section and click 'Take Photo Sample'.\n\n"
            "Q2: Why is my face not recognized?\n"
            "A2: Make sure you have registered and the lighting is good.\n\n"
            "Q3: How do I contact support?\n"
            "A3: Email us at kantjuhi04@gmail.com or use the contact form.\n\n"
            "Q4: Can I update my registered face?\n"
            "A4: Yes, just retake your photo sample in the User section.\n\n"
            "Q5: What file format are attendance records saved in?\n"
            "A5: Attendance is saved as a CSV file in the application folder.\n\n"
            "Q6: I forgot my roll number. What should I do?\n"
            "A6: Please contact your administrator or teacher for assistance."
        )
        faq_lbl = Label(self.root, text=faq_text, font=("times new roman", 16), fg="#333", justify="left", anchor="nw", bg="#ffffff")
        faq_lbl.place(x=faq_frame_x, y=110, width=500, height=350)

if __name__ == "__main__":
    root = Tk()
    app = Help(root)
    root.mainloop()