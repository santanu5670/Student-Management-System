from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from tkcalendar import DateEntry #pip install tkcalendar
import mysql.connector
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x1000')
        self.minsize(844,344)
        self.title('Student Management System')
        self.Header()
        self.Body()
        self.student_portal()
        self.department_portal()
        self.student_field()
        self.department_field()
        self.student_listbox()
        self.department_listbox()
    def Header(self):
        #Header Position
        p1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\logo1.png")
        self.iconphoto(False,p1)
        f1=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        f1.place(x=0,y=0,width=1500,height=80)
        self.photo1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\logo2.png")
        Label(f1,image=self.photo1,bg="white",width=80,height=80).place(x=30,y=0)
        # self.l1.pack(side=LEFT)
        Label(f1,text="Student Management System",fg='#1E90FF',background="white",font=('Times New Roman',40)).place(x=400,y=5)
    def Body(self):
        self.f2=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f2.place(x=0,y=80,width=850,height=350)

        self.f3=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f3.place(x=850,y=80,width=620,height=350)

        self.f4=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f4.place(x=0,y=428,width=850,height=50)

        self.f5=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f5.place(x=850,y=428,width=530,height=50)

        self.f6=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f6.place(x=0,y=473,width=850,height=232)

        self.f7=Frame(self,background="white",borderwidth=1,relief=GROOVE)
        self.f7.place(x=850,y=473,width=515,height=232)

    def student_portal(self):
        Label(self.f2,text="Student Portal",bg="white",fg='#1E90FF',font=('Times New Roman',20)).place(x=300,y=5)
        Label(self.f2,text="Student Name : ",bg="white",font=('Times New Roman',15)).place(x=15,y=50)
        Label(self.f2,text="Date of Birth : ",bg="white",font=('Times New Roman',15)).place(x=390,y=50)
        Label(self.f2,text="Age : ",bg="white",font=('Times New Roman',15)).place(x=15,y=90)
        Label(self.f2,text="Email : ",bg="white",font=('Times New Roman',15)).place(x=390,y=90)
        Label(self.f2,text="Gender : ",bg="white",font=('Times New Roman',15)).place(x=15,y=130)
        Label(self.f2,text="Contact No : ",bg="white",font=('Times New Roman',15)).place(x=390,y=130)
        Label(self.f2,text="Course Name : ",bg="white",font=('Times New Roman',15)).place(x=15,y=170)
        Label(self.f2,text="Duration : ",bg="white",font=('Times New Roman',15)).place(x=390,y=170)  
        Label(self.f2,text="Entry Year : ",bg="white",font=('Times New Roman',15)).place(x=15,y=210)
        Label(self.f2,text="Passout year : ",bg="white",font=('Times New Roman',15)).place(x=390,y=210)
        Label(self.f2,text="Address : ",bg="white",font=('Times New Roman',15)).place(x=15,y=250) 

    def student_field(self):
        #--------------Create variable--------------#
        self.name_var=StringVar()
        self.dob_var=StringVar()
        self.age_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_no_var=StringVar()
        # self.course_var=StringVar()
        self.duration_var=StringVar()
        self.entry_year_var=StringVar()
        self.passout_year_var=StringVar()
        self.address_var=StringVar()
        

        #--------------Create Entry Widget----------#
        self.name=Entry(self.f2,textvariable=self.name_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.name.place(x=150,y=53)
        self.dob=DateEntry(self.f2,textvariable=self.dob_var,width=20,font=(12),state='readonly')
        self.dob.place(x=515,y=53)
        self.age=Entry(self.f2,textvariable=self.age_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.age.place(x=150,y=93)
        self.email=Entry(self.f2,textvariable=self.email_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.email.place(x=515,y=93)
        self.gender=Combobox(self.f2,textvariable=self.gender_var,font=("Times New Roman",14),state='readonly')
        self.gender['values']=['Select','Male','Female']
        self.gender.place(x=150,y=133)
        self.gender.current(0)
        self.contact_no=Entry(self.f2,textvariable=self.contact_no_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.contact_no.place(x=515,y=133)
        # self.course=Combobox(self.f2,textvariable=self.course_var,font=("Times New Roman",14),state='readonly')
        # self.course['values']=['Select','BCA','MCA','BTECH','MTECH','BBA','MBA']
        # self.course.place(x=150,y=173)
        # self.course.current(0)
        self.duration=Combobox(self.f2,textvariable=self.duration_var,font=("Times New Roman",14),state='readonly')
        self.duration['values']=['Select','2','3','4']
        self.duration.place(x=515,y=173)
        self.duration.current(0)
        self.entry_year=Entry(self.f2,textvariable=self.entry_year_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.entry_year.place(x=150,y=213)
        self.passout_year=Entry(self.f2,textvariable=self.passout_year_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.passout_year.place(x=515,y=213)
        self.address=Text(self.f2,width=20,height=4,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.address.place(x=150,y=250)

        connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
        mycursor_fetch=connection.cursor()
        query_fetch='select department_name from Department_College'
        mycursor_fetch.execute(query_fetch)
        rows=mycursor_fetch.fetchall()
        # print(rows)
        self.course_var=StringVar()
        values1=['Select']
        # print(values1)
        for i in range(0,len(rows)):
            values1.append(rows[i])
        # print(values1)
        self.course=Combobox(self.f2,textvariable=self.course_var,values=values1,font=("Times New Roman",14),state='readonly')
        self.course.place(x=150,y=173)
        self.course.current(0)

    def department_portal(self):
        Label(self.f3,text="Department Portal",bg="white",fg='#1E90FF',font=('Times New Roman',19)).place(x=170,y=5)
        Label(self.f3,text="Department Code: ",bg="white",font=('Times New Roman',15)).place(x=15,y=50)
        Label(self.f3,text="Department Name: ",bg="white",font=('Times New Roman',15)).place(x=15,y=90)
        Label(self.f3,text="Starting Date: ",bg="white",font=('Times New Roman',15)).place(x=15,y=130)
        Label(self.f3,text="HOD Name: ",bg="white",font=('Times New Roman',15)).place(x=15,y=170)
        Label(self.f3,text="Total Teachers: ",bg="white",font=('Times New Roman',15)).place(x=15,y=210)
        Label(self.f3,text="About: ",bg="white",font=('Times New Roman',15)).place(x=15,y=250)

    def department_field(self):
        #--------------Create variable--------------#

        self.department_code_var=StringVar()
        self.department_name_var=StringVar()
        self.starting_date_var=StringVar()
        self.hod_name_var=StringVar()
        self.no_of_teachers_var=StringVar()

        #--------------Create Entry Widget----------#

        self.department_code=Entry(self.f3,textvariable=self.department_code_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.department_code.place(x=180,y=53)
        self.department_name=Entry(self.f3,textvariable=self.department_name_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.department_name.place(x=180,y=93)
        self.starting_date=DateEntry(self.f3,textvariable=self.starting_date_var,font=("Times New Roman",13),width=20,state='readonly')
        self.starting_date.place(x=180,y=133)
        self.hod_name=Entry(self.f3,textvariable=self.hod_name_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.hod_name.place(x=180,y=173)
        self.no_of_teachers=Entry(self.f3,textvariable=self.no_of_teachers_var,font=("Times New Roman",15),bg="#F5F5F5",borderwidth=0)
        self.no_of_teachers.place(x=180,y=213)
        self.about=Text(self.f3,font=("Times New Roman",15),width=20,height=4,bg="#F5F5F5",borderwidth=0)
        self.about.place(x=180,y=253)

    def student_listbox(self):
        scroll_x=Scrollbar(self.f6,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.f6,orient=VERTICAL)
        self.student_table=ttk.Treeview(self.f6,columns=("Id","Name","DOB","Age","Email","Gender","Contact No","Course Name","Duration","Entry Year","Passout Year","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Id",text="Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("DOB",text="D.O.B")
        self.student_table.heading("Age",text="Age")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact No",text="Contact No")
        self.student_table.heading("Course Name",text="Course Name")
        self.student_table.heading("Duration",text="Duration")
        self.student_table.heading("Entry Year",text="Entry Year")
        self.student_table.heading("Passout Year",text="Pasout Year")
        self.student_table.heading("Address",text="Address")

        self.student_table['show']='headings'

        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Age",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact No",width=100)
        self.student_table.column("Course Name",width=100)
        self.student_table.column("Duration",width=100)
        self.student_table.column("Entry Year",width=100)
        self.student_table.column("Passout Year",width=100)
        self.student_table.column("Address",width=100)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.student_table.pack()


    def department_listbox(self):
        scroll_x1=Scrollbar(self.f7,orient=HORIZONTAL)
        scroll_y1=Scrollbar(self.f7,orient=VERTICAL)
        self.student_table1=ttk.Treeview(self.f7,columns=("DId","DCode","DName","DDate","DHOD_Name","DTotal_Teachers","DAbout"),xscrollcommand=scroll_x1.set,yscrollcommand=scroll_y1.set)
        scroll_x1.pack(side=BOTTOM,fill=X)
        scroll_y1.pack(side=RIGHT,fill=Y)
        scroll_x1.config(command=self.student_table1.xview)
        scroll_y1.config(command=self.student_table1.yview)
        self.student_table1.heading("DId",text="Id")
        self.student_table1.heading("DCode",text="Department Code")
        self.student_table1.heading("DName",text="Department Name")
        self.student_table1.heading("DDate",text="Starting Date")
        self.student_table1.heading("DHOD_Name",text="HOD Name")
        self.student_table1.heading("DTotal_Teachers",text="Total Teachers")
        self.student_table1.heading("DAbout",text="About")

        self.student_table1['show']='headings'

        self.student_table1.column("DCode",width=110)
        self.student_table1.column("DId",width=100)
        self.student_table1.column("DName",width=110)
        self.student_table1.column("DDate",width=100)
        self.student_table1.column("DHOD_Name",width=100)
        self.student_table1.column("DTotal_Teachers",width=100)
        self.student_table1.column("DAbout",width=100)
        self.fetch_data_department()
        self.student_table1.bind("<ButtonRelease-1>",self.get_cursor_department)
        self.student_table1.pack()

