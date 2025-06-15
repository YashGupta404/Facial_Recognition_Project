from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector


class User:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0") 
        
        # variable declaration
        self.var_dep = StringVar()
        self.var_course = StringVar()  
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_studentID = StringVar()
        self.var_studentname = StringVar()
        self.var_studentdiv = StringVar()
        self.var_studentroll = StringVar()
        self.var_studentgender = StringVar()
        self.var_studentdob = StringVar()
        self.var_studentemail = StringVar()
        self.var_studentphone = StringVar()
        self.var_studentaddress = StringVar()
        self.var_studentteacher = StringVar()
      
        
    
        
        #background image
        bg_img = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg") 
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img) 
        self.lbl_bg = Label(self.root, image= self.photobg_img)
        self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
        #logo image
        image = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg")
        image = image.resize((100, 100), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image) 
        self.lbl_image = Label(self.root, image= self.photoimage)
        self.lbl_image.place(x=1420, y=10, width=100, height=100)

        #title
        title_lbl=Label(self.lbl_bg, text="User detail", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #frame
        main_frame=Frame(self.lbl_bg, bd=2, bg="white")
        main_frame.place(x=20, y = 55, width=1480,height=600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y = 10, width=730, height=580)
        img_left=Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)
        
        #current course
        curr_frame=LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Details", font=("times new roman", 12, "bold"))
        curr_frame.place( x = 5, y = 135, width=720, height=200)

        #dept
        dep_label=Label (curr_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0,column=0, padx=10, sticky=W)
        dep_combo=ttk.Combobox(curr_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)
        
        #course
        course_label=Label (curr_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0,column=2, padx=10, sticky=W)
        course_combo=ttk.Combobox(curr_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"]=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        #year
        yr_label=Label (curr_frame, text="Year",font=("times new roman", 12, "bold"), bg="white")
        yr_label.grid(row=1,column=0, padx=10, sticky=W)
        yr_combo=ttk.Combobox(curr_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        yr_combo["values"]=("Select Year", "1", "2", "3", "4")
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        #Sem
        sem_label=Label (curr_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1,column=2, padx=10, sticky=W)
        sem_combo=ttk.Combobox(curr_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"]=("Select Semester", "1", "2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

        #class student info
        cls_frame=LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        cls_frame.place( x = 5, y = 250, width=720, height=300)

        #id
        studentId_label=Label(cls_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        self.studentID_entry=ttk.Entry (cls_frame, textvariable=self.var_studentID, width=20, font=("times new roman", 13, "bold"))
        self.studentID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)
        
        #name
        studentname_label=Label(cls_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, sticky=W)
        self.studentname_entry=ttk.Entry (cls_frame,textvariable=self.var_studentname,  width=20, font=("times new roman", 13, "bold"))
        self.studentname_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)
        
        #class
        studentclass_label=Label(cls_frame, text="Student Class:",  font=("times new roman", 13, "bold"), bg="white")
        studentclass_label.grid(row=1, column=0, padx=10, sticky=W)
        classdiv_combo=ttk.Combobox(cls_frame, textvariable=self.var_studentdiv, font=("times new roman", 12, "bold"), state="readonly", width=20)
        classdiv_combo["values"]=("Select division","A", "B", "C", "D", "E")
        classdiv_combo.current(0)
        classdiv_combo.grid(row=1,column=1, padx=2, pady=5, sticky=W)
        #self.studentclass_entry=ttk.Entry (cls_frame,textvariable=self.var_studentdiv, width=20, font=("times new roman", 13, "bold"))
        #self.studentclass_entry.grid(row=1,column=1, padx=10, pady=5, sticky=W)
        
        #roll
        studentroll_label=Label(cls_frame, text="Student Roll no:", font=("times new roman", 13, "bold"), bg="white")
        studentroll_label.grid(row=1, column=2, padx=10, sticky=W)
        self.studentroll_entry=ttk.Entry (cls_frame, textvariable=self.var_studentroll,width=20, font=("times new roman", 13, "bold"))
        self.studentroll_entry.grid(row=1,column=3, padx=10, pady=5, sticky=W)
        
        #gender
        studentgender_label=Label(cls_frame, text="Student Gender:", font=("times new roman", 13, "bold"), bg="white")
        studentgender_label.grid(row=2, column=0, padx=10, sticky=W)
        Gender_combo=ttk.Combobox(cls_frame, textvariable=self.var_studentgender, font=("times new roman", 12, "bold"), state="readonly", width=20)
        Gender_combo["values"]=("Select Gender", "Male", "Female", "others", "prefer not to answer")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1, padx=2, pady=5, sticky=W)
        #self.studentgender_entry=ttk.Entry (cls_frame, textvariable=self.var_studentgender,width=20, font=("times new roman", 13, "bold"))
        #self.studentgender_entry.grid(row=2,column=1, padx=10, pady=5, sticky=W)
        
        #dob
        studentdob_label=Label(cls_frame, text="Student DOB:", font=("times new roman", 13, "bold"), bg="white")
        studentdob_label.grid(row=2, column=2, padx=10, sticky=W)
        self.studentdob_entry=ttk.Entry (cls_frame, textvariable=self.var_studentdob,width=20, font=("times new roman", 13, "bold"))
        self.studentdob_entry.grid(row=2,column=3, padx=10, pady=5, sticky=W)
        
        #email
        studentmail_label=Label(cls_frame, text="Student Email:", font=("times new roman", 13, "bold"), bg="white")
        studentmail_label.grid(row=3, column=0, padx=10, sticky=W)
        self.studentmail_entry=ttk.Entry (cls_frame, textvariable=self.var_studentemail,width=20, font=("times new roman", 13, "bold"))
        self.studentmail_entry.grid(row=3,column=1, padx=10, pady=5, sticky=W)
        
        #phone
        studentph_label=Label(cls_frame, text="Student Phone No:", font=("times new roman", 13, "bold"), bg="white")
        studentph_label.grid(row=3, column=2, padx=10, sticky=W)
        self.studentph_entry=ttk.Entry (cls_frame, textvariable=self.var_studentphone,width=20, font=("times new roman", 13, "bold"))
        self.studentph_entry.grid(row=3,column=3, padx=10, pady=5, sticky=W)
        
        #address
        studentadd_label=Label(cls_frame, text="Student Address:", font=("times new roman", 13, "bold"), bg="white")
        studentadd_label.grid(row=4, column=0, padx=10, sticky=W)
        self.studentadd_entry=ttk.Entry (cls_frame, textvariable=self.var_studentaddress,width=20, font=("times new roman", 13, "bold"))
        self.studentadd_entry.grid(row=4,column=1, padx=10, pady=5, sticky=W)
        
        #Teacher name
        teacher_label=Label(cls_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, sticky=W)
        self.teacher_entry=ttk.Entry (cls_frame,textvariable=self.var_studentteacher, width=20, font=("times new roman", 13, "bold"))
        self.teacher_entry.grid(row=4,column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(cls_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6,column=0)
        
        radionbtn2=ttk.Radiobutton(cls_frame, variable=self.var_radio1,text="No Photo Sample", value="No")
        radionbtn2.grid(row=6,column=1)
        
        #bbuttons frame
        btn_frame=Frame(cls_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame, text="Save", command=self.Add_data,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        upd_btn=Button(btn_frame, text="Update", command=self.update_data,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        upd_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,command=self.delete_data, text="Delete", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        del_btn.grid(row=0,column=2)

        res_btn=Button(btn_frame, text="Reset", command=self.reset_data,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        res_btn.grid(row=0,column=3)

        btn_frame1=Frame(cls_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y = 10, width=720, height=580)
        img_right=Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg")
        img_right=img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_right=ImageTk. PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)

        #search system
        search_frame=LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place( x = 5, y = 150, width=710, height=70)

        search_label=Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo=ttk.Combobox (search_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        search_combo ["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)
        
        search_entry=ttk.Entry (search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2, padx=10, pady=5, sticky=W)
        
        search_btn=Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3, padx=4)
        
        showAll_btn=Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        #table frame
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5,y=210, width=710, height=350)
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
       
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #function declaration
    def Add_data(self):
        if self.studentID_entry.get()=="" or self.studentname_entry.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password ="Ritikantjuhi@1234",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.studentID_entry.get(),
                self.studentname_entry.get(),
                self.studentclass_entry.get(),
                self.studentroll_entry.get(),
                self.studentgender_entry.get(),
                self.studentdob_entry.get(),
                self.studentmail_entry.get(),
                self.studentph_entry.get(),
                self.studentadd_entry.get(),
                self.var_studentteacher.get(),
                self.var_radio1.get()
            ))
                conn.commit()
             
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
    #fetching data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password ="Ritikantjuhi@1234",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from user")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()        
    # cursor at student_table
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]     
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_studentID.set(data[4])
        self.var_studentname.set(data[5])
        self.var_studentdiv.set(data[6])
        self.var_studentroll.set(data[7])
        self.var_studentgender.set(data[8])
        self.var_studentdob.set(data[9])
        self.var_studentemail.set(data[10])
        self.var_studentphone.set(data[11])
        self.var_studentaddress.set(data[12])
        self.var_studentteacher.set(data[13])
        self.var_radio1.set(data[14])
    
    # update function
    def update_data(self):
       if self.studentID_entry.get()=="" or self.studentname_entry.get()=="" or self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
       else:
           
        try:
            update = messagebox.askyesno("Update" , "do you want to update" , parent = self.root)
            if update:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ritikantjuhi@1234",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE user SET dep=%s, course=%s, year=%s, semester=%s, Name=%s, roll=%s, `div`=%s, gender=%s, email=%s, dob=%s, phone=%s, address=%s, teacher=%s, photosample=%s WHERE ID=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_studentname.get(),
                        
                        self.var_studentroll.get(),
                        self.var_studentdiv.get(),
                        self.var_studentgender.get(),
                        self.var_studentemail.get(),
                        self.var_studentdob.get(),
                      
                        self.var_studentphone.get(),
                        self.var_studentaddress.get(),
                        self.var_studentteacher.get(),
                        self.var_radio1.get(),
                        self.var_studentID.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
            else:
                return
          
            
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
    # delete function
    def delete_data(self):
        if self.var_studentID.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete", parent=self.root)
        else:
            try:
                delete_confirm = messagebox.askyesno("Delete", "Do you really want to delete this record?", parent=self.root)
                if delete_confirm:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Ritikantjuhi@1234",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM user WHERE id=%s", (self.var_studentID.get(),))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
    
    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_studentID.set("")
        self.var_studentname.set("")
        self.var_studentdiv.set("Select division")
        self.var_studentroll.set("")
        self.var_studentgender.set("Select Gender")
        self.var_studentdob.set("")
        self.var_studentemail.set("")
        self.var_studentphone.set("")
        self.var_studentaddress.set("")
        self.var_studentteacher.set("")
        self.var_radio1.set("")



if __name__ == "__main__":
    root = Tk()
    app = User(root)
    root.mainloop()        
       