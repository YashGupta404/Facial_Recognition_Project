from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = [] # to store data from database


class Attendance_management:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Attendance management System") 
        self.root.geometry("1530x790+0+0") 
        
        #==============================variables===================
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
          #background image
        bg_img = Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg") 
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img) 
        self.lbl_bg = Label(self.root, image= self.photobg_img)
        self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
    

        #title
        title_lbl=Label(self.lbl_bg, text="Attendance Management System", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #frame
        main_frame=Frame(self.lbl_bg, bd=2, bg="white")
        main_frame.place(x=20, y = 55, width=1480,height=600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y = 10, width=730, height=580)
        img_left=Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)
        
        left_inside_frame=Frame(Left_frame, bd=2, bg="white",relief=RIDGE)
        left_inside_frame.place(x=0, y = 135, width=720,height=300)
        #ID
        AttId_label=Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        AttId_label.grid(row=0, column=0, padx=10, sticky=W)
        self.studentID_entry=ttk.Entry (left_inside_frame,  width=20, textvariable=self.var_atten_id,font=("times new roman", 13, "bold"))
        self.studentID_entry.grid(row=0,column=1, pady=8)
        
        #name
        name_label=Label(left_inside_frame, text=" Name:", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, sticky=W)
        self.attname_entry=ttk.Entry (left_inside_frame,  width=20,textvariable=self.var_atten_name, font=("times new roman", 13, "bold"))
        self.attname_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)
        
        #roll
        attroll_label=Label(left_inside_frame, text="Roll no:", font=("times new roman", 13, "bold"), bg="white")
        attroll_label.grid(row=1, column=0, padx=10, sticky=W)
        self.attroll_entry=ttk.Entry (left_inside_frame,width=20,textvariable=self.var_atten_roll, font=("times new roman", 13, "bold"))
        self.attroll_entry.grid(row=1,column=1,  pady=8)
        
        #dept
        deplabel=Label (left_inside_frame, text="Department:", font=("comicsansns 11 bold", 11, "bold"), bg="white")
        deplabel.grid(row=1,column=2)
        self.att_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        self.att_dep.grid(row=1,column=3)
        
        #time
        timelabel=Label (left_inside_frame, text="Time:", font=("comicsansns 11 bold", 11, "bold"), bg="white")
        timelabel.grid(row=2,column=0,padx=10, sticky=W)
        self.att_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        self.att_time.grid(row=2,column=1)
        
        #date
        dateLabel=Label (left_inside_frame, text="Date:", font=("comicsansns 11 bold", 11, "bold"), bg="white")
        dateLabel.grid(row=2,column=2,padx=10, sticky=W)
        self.att_dt=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        self.att_dt.grid(row=2,column=3)
        
        #attendance
        attLabel=Label (left_inside_frame, text="Attendance:", font=("comicsansns 11 bold", 11, "bold"), bg="white")
        attLabel.grid(row=3,column=0,padx=10, sticky=W)
        self.attendance_status = StringVar()
        self.att_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.att_combo["values"] = ("Present", "Absent", "Leave")
        self.att_combo.current(0)
        self.att_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        
        #bbuttons frame
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame, text="Import csv",command=self.import_csv,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        upd_btn=Button(btn_frame, text="Export csv",command=self.export_csv,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        upd_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        del_btn.grid(row=0,column=2)

        res_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        res_btn.grid(row=0,column=3)

        
        
        
        
         #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance table", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y = 10, width=720, height=580)
        img_right=Image.open(r"Facial_Recognition_App\images_face_recog\background.jpg")
        img_right=img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_right=ImageTk. PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=455)
        
        
        #scroll bar
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)  # Bind the click event to get_cursor method
        
    # ====================fetch data==========================
    def fetch_data(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for row in rows:
        self.AttendanceReportTable.insert("", END, values=row)
    
    
    #import csv    
    def import_csv(self):
      global mydata
      mydata.clear()  # Clear previous data
      fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
      with open(fln, newline="\n") as myfile:
        csvread = csv.reader(myfile, delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetch_data(mydata)
      
    #export csv
    def export_csv(self):
      try:
        if len(mydata) < 1:
          messagebox.showerror("No Data", "No data found to export", parent=self.root)
          return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln, mode="w", newline="\n") as myfile:
          exp_write = csv.writer(myfile, delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+" successfully", parent=self.root)
      except Exception as es:
        messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root) 
            
    def get_cursor(self,event=""):
      cursor_row = self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
      row = content["values"]
      self.var_atten_id.set(row[0])
      self.var_atten_roll.set(row[1])
      self.var_atten_name.set(row[2])
      self.var_atten_dep.set(row[3])
      self.var_atten_time.set(row[4])
      self.var_atten_date.set(row[5])
      self.var_atten_attendance.set(row[6])
      
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")
      
            
          
        
      
      
      
    
        
        
        
        
    
    



if __name__ == "__main__":
    root = Tk()  
    app = Attendance_management(root)
    root.mainloop()  