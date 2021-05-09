from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class login_window:
   def __init__(self,root):
       self.root=root
       self.root.title("Login")
       self.root.geometry("1550x800+0+0")

       self.bg= ImageTk.PhotoImage(file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\1.jpg")
       
       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


       frame=Frame(self.root,bg="black")
       frame.place(x=610,y=170,width=340,height=450)
       
       img1= Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")
       
       img1=img1.resize((100,100),Image.ANTIALIAS)
       self.photoimage1=ImageTk.PhotoImage(img1)
       lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
       lblimg1.place(x=730,y=175,width=100,height=100)

       get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="orange")
       get_str.place(x=100,y=100)
       
       #labels
       username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="orange")
       username_lbl.place(x=65,y=152)

       self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtuser.place(x=40,y=180,width=270)
         
       password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="orange")
       password_lbl.place(x=65,y=225)

       self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtpass.place(x=40,y=250,width=270)

       #icon.............
       img2= Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")
       
       img2=img2.resize((20,20),Image.ANTIALIAS)
       self.photoimage2=ImageTk.PhotoImage(img2)
       lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
       lblimg2.place(x=650,y=323,width=25,height=25)

       img3= Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\3.jpg")
       
       img3=img3.resize((20,20),Image.ANTIALIAS)
       self.photoimage3=ImageTk.PhotoImage(img3)
       lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
       lblimg3.place(x=650,y=397,width=25,height=25)
       
       #loginBuutton
       loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="orange")
       loginbtn.place(x=110,y=300,width=120,height=35)

       #registrationButton
       registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="orange",activebackground="black")
       registerbtn.place(x=15,y=350,width=160)

       #forgetpasswordButton
       forgetbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="orange",activebackground="black")
       forgetbtn.place(x=10,y=370,width=160)
    
   def login(self):
      if self.txtuser.get()=="" or self.txtpass.get()== "":
         messagebox.showerror("Error","all field required")
      elif self.txtuser.get()=="keshav45" and self.txtpass.get()=="keshav@123":
         messagebox.showinfo("success","welcome to gundrukTech")
      else:
         messagebox.showerror("Invalid","Invalid username and password")



   

if __name__ == "__main__":
   root= Tk()
   app=login_window(root)
   root.mainloop()