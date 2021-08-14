from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk #pip install pillow

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x1000+0+0')
        self.minsize(844,344)
        self['background']='#CCCCFF'
        self.title('Student Management System')
        p1=ImageTk.PhotoImage(file='E:\Python Project\Student management System\Image\\logo1.png')
        self.iconphoto(False,p1)
        self.login_from()

    def login_from(self):
        #Image for Login page
        self.left_img=PhotoImage(file="E:\Python Project\Student management System\Image\\login_background1.png")
        self.left_img_position=Label(self,image=self.left_img,background="#F5F5F5").place(x=330,y=130,width=350,height=445)

        # Login Frame
        self.frame1=Frame(self,bg="white")
        self.frame1.place(x=680,y=130,width=370,height=445)

        #--------------Row1-----------------#

        Label(self.frame1,text="LOGIN",font=("Arial",20,"bold"),bg="white",fg="#1E90FF").place(x=135,y=30)
        Label(self.frame1,text="User Name",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=100)
        self.un=Entry(self.frame1,font=("Arial",18),bg="#F5F5F5",borderwidth=0)
        self.un.place(x=54,y=135,width=250)

        #--------------Row2-----------------#

        Label(self.frame1,text="Password",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=175)
        self.ps=Entry(self.frame1,font=("Arial",18),show="*",bg="#F5F5F5",borderwidth=0)
        self.ps.place(x=54,y=210,width=250)
        
