import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as tsmg
from login import *
from signin_database import *

class Login_database(Login):
    def login_data(self):
        if self.un.get()=='':
            tsmg.showerror("Error","User name is required")
        elif self.ps.get()=='':
            tsmg.showerror("Error","Password Required")
        else:
            try:
                # -----------Connection With Database-------------
                connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')
                
                #-----------Fetch the requirement from database------------
                query1=f"select * from User where Email='{self.un.get()}' and Password='{self.ps.get()}'"

                mycursor=connection.cursor()
                mycursor.execute(query1)
                row=mycursor.fetchone()
                connection.commit()
                connection.close()
                # print(row)
                if row==None:
                    tsmg.showerror("Error","Invalid Username & Password")
                else:
                    #------------- Destroy the Login Window and open Student Management Window------------
                    self.destroy()
                    import student_management_database as smd
                    smd.student_database_connection()
                    smd.mainloop()
            except Error as e:
                tsmg.showerror("Error",f"Error Due to {str(e)}")
        
    def signin_window(self):
        self.destroy()
        import signin_database as sd
        sd.connection_signin()
        sd.mainloop()
    def forgot_window(self):
        self.destroy()
        import forgot_password as fp
        fp.Forgot_Password()
        fp.mainloop()

class connection_login(Login_database):
    def __init__(self):
        super().__init__()
        #--------------Row3-----------------#

        self.btn_img1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\Login.png")
        self.btn=Button(self.frame1,image=self.btn_img1,bd=0,bg="white",activebackground="white",cursor="hand2",command=self.login_data).place(x=41,y=255)

        #--------------Row4-----------------#
        Label(self.frame1,text="New User?",bg="white").place(x=50,y=350)
        self.signup=Button(self.frame1,text="Signup",bg="white",bd=0,activebackground="white",fg='blue',activeforeground='blue',cursor="hand2",command=self.signin_window).place(x=110,y=350)
        self.forgot_password=Button(self.frame1,text="Forgot your password?",bg="white",bd=0,activebackground="white",fg='blue',activeforeground='blue',cursor="hand2",command=self.forgot_window).place(x=50,y=380)
    
if __name__=='__main__':
    window=connection_login()
    window.mainloop()