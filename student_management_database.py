import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as tsmg
from tkinter import filedialog
from student_management import *
from tkinter import simpledialog
import csv
import  os
mydata=[]
mydata_department=[]

class student_database(GUI):
    #----------------------------------Student Portal------------------------------------#
    def insert_data(self):
        if self.name.get()=='' or self.age.get()=='' or self.email.get()=='' or self.gender.get()=='Select' or self.contact_no.get()=='' or self.course.get()=='Select' or self.duration.get()=='Select' or self.entry_year.get()=='' or self.passout_year.get()=='' or self.address.get('1.0',END)=='':
            tsmg.showerror("Error","All fields are required")
        else:
            try:
                #------------Connection With Database-----------#
                connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                #------------Create Table-----------#
                query_create_table='''create table if not exists Student_College
                (Student_id integer primary key auto_increment,
                Name varchar(60) not null,
                DOB DATE not null,
                Age integer not null,
                Email varchar(60) UNIQUE not null,
                Gender varchar(10) not null,
                Contact_number int(15) not null,
                Course varchar(40) not null,
                Duration integer not null,
                Entry_year varchar(20) not null,
                Passout_year varchar(20) not null,
                Address varchar(100) not null)''' #int(11) means maximum value will be 10
                mycursor=connection.cursor()
                mycursor.execute(query_create_table)
                connection.close()

                #------------Insert Data-----------#

                connection1=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')                
                query_insert='''insert into Student_College(Name,DOB,Age,Email,Gender,Contact_number,Course,Duration,
                Entry_year,Passout_year,Address)values('{}','{}',{},'{}','{}',{},'{}',{},'{}','{}','{}')'''.format(self.name.get(),self.dob.get_date(),self.age.get(),self.email.get(),self.gender.get(),self.contact_no.get(),self.course.get(),self.duration.get(),self.entry_year.get(),self.passout_year.get(),self.address.get('1.0',END))
                mycursor_insert=connection1.cursor()
                mycursor_insert.execute(query_insert)
                connection1.commit()
                self.fetch_data()
                self.clear()
                connection1.close()

            except Error as e:
                tsmg.showerror("Error",f"Error Occur Due to {str(e)}")
    
    def fetch_data(self):
        connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
        mycursor_fetch=connection.cursor()
        query_fetch='select * from Student_College'
        mycursor_fetch.execute(query_fetch)
        rows=mycursor_fetch.fetchall()
        global mydata
        mydata=rows
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                connection.commit()
        connection.close()

    def clear(self):
        self.name_var.set("")
        self.dob_var.set("")
        self.age_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select")
        self.contact_no_var.set("")
        self.course_var.set("Select")
        self.duration_var.set("Select")
        self.entry_year_var.set("")
        self.passout_year_var.set("")
        self.address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        # print(row)
        self.name_var.set(row[1])
        self.dob_var.set(row[2])
        self.age_var.set(row[3])
        self.email_var.set(row[4])
        self.gender_var.set(row[5])
        self.contact_no_var.set(row[6])
        self.course_var.set(row[7])
        self.duration_var.set(row[8])
        self.entry_year_var.set(row[9])
        self.passout_year_var.set(row[10])
        self.address.delete('1.0',END)
        self.address.insert(END,row[11])
    def open_popup(self):
        self.id=simpledialog.askinteger("Id","Please enter Student id")
        # print(id)
    def update(self):
        try:
            self.open_popup()
            connection_update=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
            update_query=f'''update Student_college set Name='{self.name.get()}',DOB='{self.dob.get_date()}'
            ,Age={self.age.get()},Email='{self.email.get()}',Gender='{self.gender.get()}',Contact_number={self.contact_no.get()},
            Course='{self.course.get()}',Duration={self.duration.get()},Entry_year={self.entry_year.get()},
            Passout_year={self.passout_year.get()},Address='{self.address.get('1.0',END)}' where Student_id={self.id}'''
            mycursor_update=connection_update.cursor()
            mycursor_update.execute(update_query)
            connection_update.commit()
            connection_update.close()
            self.fetch_data()
            # self.get_cursor()
        except Error as e:
            tsmg.showerror("Error","Something went to wrong please try again leter")
    
    def delete(self):
        try:
            self.open_popup()
            val=tsmg.askquestion("Confirm","Do you want to delete?")
            if val=='yes':
                connection_delete=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                delete_query=f'''delete from Student_College where Student_id={self.id}'''
                mycursor_delete=connection_delete.cursor()
                mycursor_delete.execute(delete_query)
                connection_delete.commit()
                connection_delete.close()
                self.fetch_data()
                self.clear()
        except Error as e:
            tsmg.showerror("Error","Something went to wrong please try again leter")
    def download(self):
        try:
            mydata1=[('Id','Name','D.O.B','Age','Email','Gender','Contact No','Course','Duration','Entry Year','Passout Year','Address')]
            if len(mydata)<1:
                tsmg.showerror("Error","No data available for download")
            else:
                f_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("csv files","*.csv"),("All Files","*.*"),))
                with open(f_name,mode='w') as myfile:
                    exp_writer=csv.writer(myfile,delimiter=',')
                    for i in mydata1:
                        exp_writer.writerow(i)
                    for j in mydata:
                        exp_writer.writerow(j)
        except Error as e:
            tsmg.showerror("Error",f"Error occur due to {str(e)}")

    #----------------------------------Department Portal------------------------------------#

    def insert_data_department(self):
         if self.department_code.get()=='' or self.department_name.get()=='' or self.starting_date.get()=='' or self.hod_name.get()=='Select' or self.no_of_teachers.get()=='' or self.about.get('1.0',END)=='':
            tsmg.showerror("Error","All fields are required")
         else:
            try:
                #------------Connection With Database-----------#
                connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                #------------Create Table-----------#
                query_create_table='''create table if not exists Department_College
                (Department_Id integer primary key auto_increment,
                Department_Code varchar(20) UNIQUE not null,
                Department_Name varchar(40) not null,
                Starting_Date DATE not null,
                HOD_Name varchar(40) not null,
                Total_Number_Teacher int(15) not null,
                About varchar(100) not null
                )''' #int(11) means maximum value will be 10
                mycursor=connection.cursor()
                mycursor.execute(query_create_table)
                connection.close()

                #------------Insert Data-----------#

                connection1=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')                
                query_insert='''insert into Department_College(Department_Code,Department_Name,Starting_Date,Hod_Name,Total_Number_Teacher,About)values('{}','{}','{}','{}',{},'{}')'''.format(self.department_code.get(),self.department_name.get(),self.starting_date.get_date(),self.hod_name.get(),self.no_of_teachers.get(),self.about.get('1.0',END))
                mycursor_insert=connection1.cursor()
                mycursor_insert.execute(query_insert)
                connection1.commit()
                self.fetch_data_department()
                self.clear_department()
                connection1.close()
                self.student_field()
            except Error as e:
                tsmg.showerror("Error",f"Error Occur Due to {str(e)}")

    def fetch_data_department(self):
        connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
        mycursor_fetch=connection.cursor()
        query_fetch='select * from Department_College'
        mycursor_fetch.execute(query_fetch)
        rows=mycursor_fetch.fetchall()
        global mydata_department
        mydata_department=rows
        if len(rows)!=0:
            self.student_table1.delete(*self.student_table1.get_children())
            for row in rows:
                self.student_table1.insert('',END,values=row)
                connection.commit()
        connection.close()

    def clear_department(self):
        self.department_code_var.set("")
        self.department_name_var.set("")
        self.starting_date_var.set("")
        self.hod_name_var.set("")
        self.no_of_teachers_var.set("")
        self.about.delete("1.0",END)

    def get_cursor_department(self,ev):
        cursor_row=self.student_table1.focus()
        contents=self.student_table1.item(cursor_row)
        row=contents['values']
        # print(row)
        self.department_code_var.set(row[1])
        self.department_name_var.set(row[2])
        self.starting_date_var.set(row[3])
        self.hod_name_var.set(row[4])
        self.no_of_teachers_var.set(row[5])
        self.about.delete('1.0',END)
        self.about.insert(END,row[6])

    def open_popup_department(self):
        self.id_department=simpledialog.askinteger("Id","Please enter department id")

    def update_department(self):
        try:
            self.open_popup_department()
            connection_update=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
            update_query=f'''update Department_college set Department_Code='{self.department_code.get()}',Department_Name='{self.department_name.get()}'
            ,Starting_Date='{self.starting_date.get_date()}',HOD_Name='{self.hod_name.get()}',Total_Number_Teacher='{self.no_of_teachers.get()}',About='{self.about.get('1.0',END)}' where Department_Id={self.id_department}'''
            mycursor_update=connection_update.cursor()
            mycursor_update.execute(update_query)
            connection_update.commit()
            connection_update.close()
            self.fetch_data_department()
            self.student_field()
            # self.get_cursor()
        except Error as e:
            tsmg.showerror("Error","Something went to wrong please try again leter")
    
    def delete_department(self):
        try:
            self.open_popup_department()
            val=tsmg.askquestion("Confirm","Do you want to delete?")
            if val=='yes':
                connection_delete=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                delete_query=f'''delete from Department_College where Department_Id={self.id_department}'''
                mycursor_delete=connection_delete.cursor()
                mycursor_delete.execute(delete_query)
                connection_delete.commit()
                connection_delete.close()
                self.fetch_data_department()
                self.clear_department()
                self.student_field()
        except Error as e:
            tsmg.showerror("Error","Something went to wrong please try again leter")
    
    def download_department(self):
        try:
            mydata1=[('Id','Department Code','Department Name','Starting Date','HOD Name','Total Teachers','About')]
            if len(mydata_department)<1:
                tsmg.showerror("Error","No data available for download")
            else:
                f_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("csv files","*.csv"),("All Files","*.*"),))
                with open(f_name,mode='w') as myfile:
                    exp_writer=csv.writer(myfile,delimiter=',')
                    for i in mydata1:
                        exp_writer.writerow(i)
                    for j in mydata_department:
                        exp_writer.writerow(j)
        except Error as e:
            tsmg.showerror("Error",f"Error occur due to {str(e)}")

class student_database_connection(student_database):
    def __init__(self):
        super().__init__()
        self.student_button()
        self.list_student_department_portion()
        self.department_button()
        # self.student_field()
        # self.search()
    def student_button(self):
        Button(self.f2,text="Add",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.insert_data).place(x=735,y=53)
        Button(self.f2,text="Update",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.update).place(x=735,y=103)
        Button(self.f2,text="Delete",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.delete).place(x=735,y=153)
        Button(self.f2,text="Clear",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.clear).place(x=735,y=203)
        Label(self.f4,text="Search By",width=10,padx=6,pady=7,bg='#306EFF',fg='white',font=('Arial',10,'bold')).place(x=10,y=6)
    def list_student_department_portion(self):
        #------------------------------student part--------------------------------#
        self.search=Combobox(self.f4,width=12,font=('Arial',19),state='readonly')
        self.search['values']=['Select','Student_id','Name','Email','Contact_number','Course']   
        self.search.place(x=120,y=6)
        self.search.current(0)
        self.search_entry=Entry(self.f4,width=13,font=('Arial',18),bg="white",borderwidth=3,relief=GROOVE)
        self.search_entry.place(x=327,y=6)  
        Button(self.f4,text="Search",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.search_data).place(x=520,y=6)
        Button(self.f4,text="Show All",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.fetch_data).place(x=630,y=6)
        Button(self.f4,text="Download",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.download).place(x=740,y=6)
        
        #-------------------------------department part-----------------------------#

        self.search_department=Combobox(self.f5,width=5,font=('Arial',19),state='readonly')
        self.search_department['values']=['Select','Department_Id','Department_Name','HOD_Name']   
        self.search_department.place(x=5,y=6)
        self.search_department.current(0)
        self.search_entry_department=Entry(self.f5,width=7,font=('Arial',18),bg="white",borderwidth=3,relief=GROOVE)
        self.search_entry_department.place(x=105,y=6)
        Button(self.f5,text="Search",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.search_data_department).place(x=210,y=6)
        Button(self.f5,text="Show All",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.fetch_data_department).place(x=310,y=6)
        Button(self.f5,text="Download",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.download_department).place(x=410,y=6)
        
    def department_button(self):
        Button(self.f3,text="Add",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.insert_data_department).place(x=400,y=53)
        Button(self.f3,text="Update",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.update_department).place(x=400,y=103)
        Button(self.f3,text="Delete",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.delete_department).place(x=400,y=153)
        Button(self.f3,text="Clear",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=self.clear_department).place(x=400,y=203)
        Button(self.f3,text="Exit",width=10,padx=6,pady=6,bg='#306EFF',fg='white',font=('Arial',10,'bold'),activebackground="#306EFF",activeforeground='white',bd=0,command=quit).place(x=400,y=253)
        

    def search_data(self):
        connection_search=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
        mycursor_search=connection_search.cursor()
        if self.search.get()=='Select':
            tsmg.showerror("Error","Invalid Option")
        else:
            query_search=f"select * from Student_College where {self.search.get()} like '{self.search_entry.get()}' "
            mycursor_search.execute(query_search)
            rows1=mycursor_search.fetchall()
            if len(rows1)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row1 in rows1:
                    self.student_table.insert('',END,values=row1)
                    connection_search.commit()
            else:
                tsmg.showinfo("Not Found","Sorry no data found")
        connection_search.close()

    def search_data_department(self):
        connection_search=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
        mycursor_search=connection_search.cursor()
        if  self.search_department.get()=='Select':
            tsmg.showerror("Error","Invalid Option")
        else:
            query_search=f"select * from Department_College where {self.search_department.get()} like '{self.search_entry_department.get()}' "
            mycursor_search.execute(query_search)
            rows1=mycursor_search.fetchall()
            if len(rows1)!=0:
                self.student_table1.delete(*self.student_table1.get_children())
                for row1 in rows1:
                    self.student_table1.insert('',END,values=row1)
                    connection_search.commit()
            else:
                tsmg.showinfo("Not Found","Sorry no data found")
        connection_search.close()

if __name__=='__main__':
    window=student_database_connection() #Here window is use as a root
    window.mainloop()
