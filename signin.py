from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk #pip install pillow
class Signin(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x1000+0+0')
        self.minsize(844,344)
        self.title('Student Management System')
        # p1=PhotoImage(file='E:\Python(6th sem)\Tkinter\Student management System\Image\\NSEC_Logo.png')
        p1=ImageTk.PhotoImage(file='E:\Python Project\Student management System\Image\\logo1.png')
        self.iconphoto(False,p1)

        #Image for siginin page
        self.left_img=PhotoImage(file="E:\Python Project\Student management System\Image\\banner-img-1 - Copy.png")
        self.left_img_position=Label(self,image=self.left_img,background="#B7CEEC").place(x=150,y=100,width=400,height=500)

        # Registration Frame
        self.frame1=Frame(self,bg="white")
        self.frame1.place(x=550,y=100,width=700,height=500)

        #--------------Row1-----------------#

        Label(self.frame1,text="REGISTER HERE",font=("Arial",20,"bold"),bg="white",fg="#1E90FF").place(x=50,y=30)
        Label(self.frame1,text="First Name",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=100)
        self.fn=Entry(self.frame1,font=("Arial",18),bg="#E5E4E2",borderwidth=0)
        self.fn.place(x=54,y=130,width=250)
        Label(self.frame1,text="Last Name",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=370,y=100)
        self.ln=Entry(self.frame1,font=("Arial",18),bg="#E5E4E2",borderwidth=0)
        self.ln.place(x=374,y=130,width=250)

        #--------------Row2-----------------#

        Label(self.frame1,text="Contact No",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=170)
        self.cn=Entry(self.frame1,font=("Arial",18),bg="#E5E4E2",borderwidth=0)
        self.cn.place(x=54,y=200,width=250)
        Label(self.frame1,text="Email",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=370,y=170)
        self.em=Entry(self.frame1,font=("Arial",18),bg="#E5E4E2",borderwidth=0)
        self.em.place(x=374,y=200,width=250)

        #--------------Row3-----------------#
 
        Label(self.frame1,text="Security Question",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=240)
        self.sq=Combobox(self.frame1,font=("Arial",18),state='readonly')
        self.sq['values']=['Select','Father Name','School Name','Date Of Birth','Your Birth Place','Lucky Number']
        self.sq.place(x=54,y=270,width=250)
        self.sq.current(0)
        Label(self.frame1,text="Answer",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=370,y=240)
        self.an=Entry(self.frame1,font=("Arial",18),bg="#E5E4E2",borderwidth=0)
        self.an.place(x=374,y=270,width=250)

        #--------------Row4-----------------#

        Label(self.frame1,text="Password",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=50,y=310)
        self.ps=Entry(self.frame1,font=("Arial",18),show="*",bg="#E5E4E2",borderwidth=0)
        self.ps.place(x=54,y=340,width=250)
        Label(self.frame1,text="Confirm Password",font=("Arial",15,"bold"),bg="white",fg="#1E90FF").place(x=370,y=310)
        self.cp=Entry(self.frame1,font=("Arial",18),show="*",bg="#E5E4E2",borderwidth=0)
        self.cp.place(x=374,y=340,width=250)

        #--------------Row5-----------------#
        self.var_chk=IntVar()
        checkbox=Checkbutton(self.frame1,text="I Agree The Terms & Condition",bg="White",variable=self.var_chk,onvalue=1,offvalue=0,font=("Arial",10,"bold"),activebackground="white")
        checkbox.place(x=50,y=380)

        

