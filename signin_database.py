import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as tsmg
from signin import *
class Signin_database(Signin):
    def siginin_data(self):
        if self.fn.get()=="":
            tsmg.showerror("error"," Name is required ")
        elif self.ln.get()=="":
            tsmg.showerror("error","Last Name is required")
        elif self.cn.get()=="":
            tsmg.showerror("error","Contact Number is required")
        elif self.em.get()=="":
            tsmg.showerror("error","Email is required")
        elif self.sq.get()=="Select":
            tsmg.showerror("error","Security question is required")
        elif self.an.get()=="":
            tsmg.showerror("error","Answer required")
        elif self.ps.get()=="":
            tsmg.showerror("error","Password is required")
        elif self.cp.get()=="":
            tsmg.showerror("error","Confirm Password is required")
        elif self.var_chk.get()==0:
             tsmg.showerror("Error","Plsease agree our terms and condition")
        elif self.ps.get()!=self.cp.get():
            tsmg.showerror("Error","Password & Confirm Password should be same")
        else:
            try:
                #------------Connection With Database-----------#
                self.connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                #------------Create Table-----------#
                query='''create table if not exists User(First_Name varchar(60) not null,
                Last_Name varchar(60) not null,
                candidate_id integer primary key auto_increment,
                Contact_number int(20) not null,
                Email varchar(60) UNIQUE not null,
                Security_Question varchar(20) not null,
                Answer varchar(60) not null,
                Password varchar(60) not null,
                Confirm_Password varchar(60) not null,
                Terms_Condition varchar(6) not null)''' #int(11) means maximum value will be 10
                mycursor=self.connection.cursor()
                mycursor.execute(query)

                #------------Insert Data-----------#
                if self.var_chk.get()==1:
                    self.chk_answer="Agree"
                query_insert="insert into User(First_Name,Last_Name,Contact_number,Email,Security_Question,Answer,Password,Confirm_Password,Terms_condition) values('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(self.fn.get(),self.ln.get(),self.cn.get(),self.em.get(),self.sq.get(),self.an.get(),self.ps.get(),self.cp.get(),self.chk_answer)
                mycursor_insert=self.connection.cursor()
                mycursor_insert.execute(query_insert)
                self.connection.commit()

                #------------Show Id-----------#
                show_id=f"select candidate_id from User where Email='{self.em.get()}'"
                mycursor_show_id=self.connection.cursor()
                mycursor_show_id.execute(show_id)
                for db in mycursor_show_id:
                    tsmg.showinfo("UserId",f"Your Id is {db}")
                self.connection.commit()
                self.connection.close()
                self.destroy()
                import student_management_database as smd
                if __name__=='__main__':
                    smd.student_database_connection()
                    smd.mainloop()
            except Error as e:
                tsmg.showerror("Error",f"{e}")

    def login_window(self):
        self.destroy()
        import login_database as ld
        if __name__=='__main__':
            ld.connection_login()
            ld.mainloop()
        
class connection_signin(Signin_database):
    def __init__(self):
        super().__init__()
        #--------------Row6-----------------#

        self.btn_img=PhotoImage(file="E:\Python Project\Student management System\Image\\register-button - Copy.png")
        self.btn1=Button(self.frame1,image=self.btn_img,bg="White",bd=0,cursor="hand2",activebackground="white",command=self.siginin_data).place(x=37,y=400)

        self.btn_img1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\Login.png")
        self.btn2=Button(self,image=self.btn_img1,bd=0,bg="#B7CEEC",activebackground="#B7CEEC",cursor="hand2",command=self.login_window)
        self.btn2.place(x=290,y=523)

if __name__=='__main__':
    window=connection_signin()
    window.mainloop()
    