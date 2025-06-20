from tkinter import* 
from PIL import Image, ImageTk 

class Team:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Team") 
        self.root.geometry("1530x790+0+0") 
        
        # Background image
        bg_img = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg") 
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img) 
        self.lbl_bg = Label(self.root, image=self.photobg_img)
        self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
        # Title with shadow effect
        shadow_lbl = Label(self.root, text="Developers", font=("times new roman", 35, "bold"), bg="#7a8ba7", fg="gray")
        shadow_lbl.place(x=4, y=4, width=1530, height=45)
        title_lbl = Label(self.root, text="Developers", font=("times new roman", 35, "bold"), bg="#acc0d3", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # --- Team Members ---
        member_width = 190
        image_size = 180
        n_members = 3
        gap = 60  # 60px gap between members
        total_width = n_members * member_width + (n_members - 1) * gap
        start_x = (1530 - total_width) // 2
        y_img = 160

        # Yash
        yash_x = start_x + (member_width - image_size)//2
        yash_img = Image.open(r"Facial_Recognition_App\images_face_recog\yash_profile.jpg") 
        yash_img = yash_img.resize((image_size, image_size), Image.LANCZOS)
        self.photoyash_img = ImageTk.PhotoImage(yash_img)
        self.yash_label = Label(self.root, image=self.photoyash_img, bd=0)
        self.yash_label.place(x=yash_x, y=y_img, width=image_size, height=image_size)
        self.yash_text = Label(self.root, text="Yash", font=("times new roman", 16, "bold"), fg="#333")
        self.yash_text.place(x=yash_x, y=y_img+image_size+10, width=image_size, height=30)
        self.yash_desc = Label(self.root,text="Lead Developer\nPython & AI Enthusiast", font=("times new roman", 12), fg="#444", justify="center")
        self.yash_desc.place(x=yash_x, y=y_img+image_size+45, width=image_size, height=40)

        # Juhi
        juhi_x = start_x + member_width + gap + (member_width - image_size)//2
        juhi_img = Image.open(r"Facial_Recognition_App\images_face_recog\Juhi_profile.jpeg")
        juhi_img = juhi_img.resize((image_size, image_size), Image.LANCZOS)
        self.photojuhi_img = ImageTk.PhotoImage(juhi_img)
        self.juhi_label = Label(self.root, image=self.photojuhi_img, bd=0)
        self.juhi_label.place(x=juhi_x, y=y_img, width=image_size, height=image_size)
        self.juhi_text = Label(self.root, text="Juhi", font=("times new roman", 16, "bold"), fg="#333")
        self.juhi_text.place(x=juhi_x, y=y_img+image_size+10, width=image_size, height=30)
        self.juhi_desc = Label(self.root, text="Frontend \n MySQL Integration", font=("times new roman", 12), fg="#444", justify="center")
        self.juhi_desc.place(x=juhi_x, y=y_img+image_size+45, width=image_size, height=40)

        # Rohit
        rohit_x = start_x + 2*(member_width + gap) + (member_width - image_size)//2
        rohit_img = Image.open(r"Facial_Recognition_App\images_face_recog\Rohit_profile.jpg") 
        rohit_img = rohit_img.resize((image_size, image_size), Image.LANCZOS)
        self.photorohit_img = ImageTk.PhotoImage(rohit_img)
        self.rohit_label = Label(self.root, image=self.photorohit_img, bd=0)
        self.rohit_label.place(x=rohit_x, y=y_img, width=image_size, height=image_size)
        self.rohit_text = Label(self.root, text="Rohit", font=("times new roman", 16, "bold"), fg="#333")
        self.rohit_text.place(x=rohit_x, y=y_img+image_size+10, width=image_size, height=30)
        self.rohit_desc = Label(self.root, text="Backend Engineer\nDatabase & API", font=("times new roman", 12), fg="#444", justify="center")
        self.rohit_desc.place(x=rohit_x, y=y_img+image_size+45, width=image_size, height=40)

if __name__ == "__main__":
    root = Tk()
    app = Team(root)
    root.mainloop()