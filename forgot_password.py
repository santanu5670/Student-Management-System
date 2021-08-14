from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk #pip install pillow
import tkinter.messagebox as tsmg
from mysql.connector import Error 
import mysql.connector

class Forgot_Password(Tk):
    def __init__(self): #window for forgot password screen
        super().__init__()
        self.geometry('1200x1000+0+0')
        self.minsize(844,344)
        self['background']='#CCCCFF'
        self.title('Student Management System')
        p1=ImageTk.PhotoImage(file='E:\Python Project\Student management System\Image\\logo1.png')
        self.iconphoto(False,p1)

        #Image for Forgot Password page
        self.left_img=PhotoImage(file="E:\Python Project\Student management System\Image\\unnamed.png")
        self.left_img_position=Label(self,image=self.left_img,background="#F5F5F5").place(x=330,y=130,width=350,height=445)

        # Forgot Password Frame
        frame1=Frame(self,bg="white")
        frame1.place(x=680,y=130,width=370,height=445)

        #--------------Row1-----------------#

        Label(frame1,text="Forgot Your Password?",font=("Arial",20,"bold"),bg="white",fg="#1E90FF").place(x=20,y=30)
        Label(frame1,text="Please put answer of your security question",font=("Arial",10),bg="White").place(x=23,y=70)

        #--------------Row2-----------------#
        Label(frame1,text="Candidate Id",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=25,y=120)
        self.cd=Entry(frame1,font=("Arial",18),bg="#F5F5F5",borderwidth=0)
        self.cd.place(x=28,y=155,width=250)

        #--------------Row3-----------------#

        Label(frame1,text="Security Question",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=25,y=195)
        self.sq=Entry(frame1,font=("Arial",18),bg="#F5F5F5",borderwidth=0)
        self.sq.place(x=28,y=230,width=250)

        #--------------Row4-----------------#

        self.btn_img1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\nxt.jpg")
        self.btn=Button(frame1,image=self.btn_img1,bd=0,bg="white",activebackground="white",cursor="hand2",command=self.forgot_data).place(x=23,y=280)

        #--------------Row5-----------------#
        self.back_to_login=Button(frame1,text="Back to Login",bg="white",fg="blue",bd=0,activebackground="white",activeforeground="blue",cursor="hand2",command=self.login_window).place(x=32,y=360)

    def forgot_data(self): #database for forgot password
        try:
            if self.cd.get()=='':
                tsmg.showerror("Error","Candidate Id Required")
            elif self.sq.get()=='':
                tsmg.showerror("Error","Sqcurity Question Required")
            else:
                connection=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')

                query=f"select * from User where candidate_id={self.cd.get()} and Answer='{self.sq.get()}' "
                mycursor=connection.cursor()
                mycursor.execute(query)
                row=mycursor.fetchone()
                connection.commit()
                connection.close()
                # print(row)

                if row==None:
                    tsmg.showerror("Error","Inavlid Candidate Id and Security question")
                else: 
                   self.reset() 
                #    self.reset_data()
        except Error as e:
            tsmg.showerror("Error",f"Error Occur due to {str(e)}")
    def login_window(self):
        self.destroy()
        import login_database as ld
        if __name__=='__main__':
            ld.connection_login()
            ld.mainloop()
    def reset(self): #window for Reset password screen
        self.geometry('1200x1000+0+0')
        self.minsize(844,344)
        self.title('Student Management System')
        self['background']='#F5F5F5'
        p2=PhotoImage(file='E:\Python Project\Student management System\Image\\NSEC_Logo.png')
        self.iconphoto(False,p2)
        #Image for Reset Password page
        self.left_img=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\forgot-password-reset.png")
        self.left_img_position=Label(self,image=self.left_img,background="#CCCCFF").place(x=330,y=130,width=350,height=445)

        # Reset Password Frame
        self.frame2=Frame(self,bg="white")
        self.frame2.place(x=680,y=130,width=370,height=445)

        #--------------Row1-----------------#

        Label(self.frame2,text="Reset Password",font=("Arial",20,"bold"),bg="white",fg="#1E90FF").place(x=23,y=30)
        Label(self.frame2,text="New Password",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=23,y=130)
        self.ps=Entry(self.frame2,font=("Arial",18),show='*',bg="#F5F5F5",borderwidth=0)
        self.ps.place(x=26,y=165,width=250)

        #--------------Row2-----------------#

        Label(self.frame2,text="Confirm New Password",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=23,y=205)
        self.cp=Entry(self.frame2,font=("Arial",18),show="*",bg="#F5F5F5",borderwidth=0)
        self.cp.place(x=26,y=240,width=250)

        self.btn_img1=ImageTk.PhotoImage(file="E:\Python Project\Student management System\Image\\continue.jpg")
        self.btn=Button(self.frame2,image=self.btn_img1,bd=0,bg="white",activebackground="white",cursor="hand2",command=self.reset_data).place(x=23,y=275)

        #--------------Row4-----------------#
        self.back_to_login=Button(self.frame2,text="Back to login",bg="white",bd=0,activebackground="white",fg="blue",activeforeground="blue",cursor="hand2",command=self.login_window).place(x=28,y=350)
    def reset_data(self): #database for reset password
        if self.ps.get()=='':
            tsmg.showerror("Error","Password required")
        elif self.cp.get()=='':
            tsmg.showerror("Error","Confirm Password required")
        elif self.ps.get()!=self.cp.get():
            tsmg.showwarning("Error","Password & Confirm Password must be same")
        else:
            try:
                # tsmg.showinfo("Candidate Id",f"Candidate id is {self.cd.get()}")
                # tsmg.showinfo("Security Question answer",f"Security Question answer is {self.sq.get()}")
                connection1=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')

                query1=f"update user set password='{self.ps.get()}' where candidate_id={self.cd.get()}"
                mycursor=connection1.cursor()
                mycursor.execute(query1)
                connection1.commit()
                connection1.close()

                connection2=mysql.connector.connect(host='localhost',port='3307',database='student_management_system',user='root',password='root')

                query2=f"update user set Confirm_Password='{self.cp.get()}' where candidate_id={self.cd.get()}"
                mycursor1=connection2.cursor()
                mycursor1.execute(query2)
                connection2.commit()
                connection2.close()
                self.login_window()

            except Error as e:
                tsmg.showerror("Error",f"Error occur due to {str(e)}")

if __name__=='__main__':
    window=Forgot_Password()
    window.mainloop()
