from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student



def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(
            file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\1.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(
            r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")

        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), bg="black", fg="orange")
        get_str.place(x=100, y=100)

        # labels
        username_lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), bg="black", fg="orange")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="black", fg="orange")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # icon.............
        img2 = Image.open(
            r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")

        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(
            r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\3.jpg")

        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=397, width=25, height=25)

        # loginBuutton
        loginbtn = Button(frame, command=self.login, text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="red", fg="orange")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registrationButton
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", 10, "bold"), borderwidth=0, bg="black", fg="orange", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forgetpasswordButton
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, bg="black", fg="orange", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "keshav45" and self.txtpass.get() == "keshav@123":
            messagebox.showinfo("success", "welcome to gundrukTech")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()

                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("Yesno","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            # self.root.destroy()

            #************************************Reaet password button ko lagi*******************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","select your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            # my_cursor.execute("select * from register where email=%s and securityQ=%s and securityA=%s "(
            # self.txtuser.get(),
            # self.combo_security_Q.get(),
            # self.txt_security.get()

            #          ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid security answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                messagebox.showinfo("Info","your password has been reset , please login new password",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()
               


                
                
 #   ************************forget password ko lagi****************
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="white", fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)





#>>>>>>>>>>>>>>>>>>>>>>>>Register ko class lyakoo>>>

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1600x500+0+0")

        # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        self.bg = ImageTk.PhotoImage(
            file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\5.jpg")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        self.bg1 = ImageTk.PhotoImage(
            file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\6.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        fname = Label(frame, text="First and middle name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # column 2
        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ...........column3
        security_Q = Label(frame, text="Select Security Question", font=(
            "times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth place", "your dad name", "your mother name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ......colum 5
        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Comform Password", font=(
            "times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # button

        img = Image.open(
            r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\7.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(
            r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\8.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login,borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)


# ................fuction

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fills are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "user already exit ,try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo("Success", "Register Successfully", parent=self.root )
            conn.commit()
            conn.close()
            # self.root.destroy()
    def return_login(self):
        self.root.destroy()
            
#>>>>>>>>>>>>>>>>>main page ko
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x720+0+0")
        self.root.title("Face Recognition System")

        # first image
        img1 = Image.open("Images/PUbanner_2.jpg")
        img1 = img1.resize((450, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=120)

        # second image
        img2 = Image.open("Images/OIP.jpeg")
        img2 = img2.resize((450, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=450, height=120)

        # third image
        img3 = Image.open("Images/ncit-wide2017-11-18.jpg")
        img3 = img3.resize((450, 120), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=450, height=120)

        # background image
        img4 = Image.open("Images/face-recognition-logo.jpeg")
        img4 = img4.resize((1350, 580), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1350, height=580)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("arial", 35, "bold"), bg="white", fg="magenta")
        title_lbl.place(x=0, y=0, width=1350, height=45)  # using .place u can place things at any part of the window

        # different buttons with images
        # student button
        img5 = Image.open("Images/student.jpg")
        img5 = img5.resize((195, 195), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        btn1.place(x=100, y=80, width=195, height=195)

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=100, y=245, width=195, height=40)

        # Face Detection button
        img6 = Image.open("Images/faceDetector.jpeg")
        img6 = img6.resize((195, 195), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        btn2.place(x=400, y=80, width=195, height=195)

        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn2_2.place(x=400, y=245, width=195, height=40)

        # attendance button
        img7 = Image.open("Images/face.jpg")
        img7 = img7.resize((195, 195), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        btn3.place(x=700, y=80, width=195, height=195)

        btn3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn3_3.place(x=700, y=245, width=195, height=40)

        # Help Desk button
        img8 = Image.open("Images/helpdesk.png")
        img8 = img8.resize((195, 195), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        btn4.place(x=1000, y=80, width=195, height=195)

        btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn4_4.place(x=1000, y=245, width=195, height=40)

        # train data button
        img9 = Image.open("Images/trainFace-khom.png")
        img9 = img9.resize((195, 195), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn5 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        btn5.place(x=100, y=350, width=195, height=195)

        btn5_5 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn5_5.place(x=100, y=525, width=195, height=40)

        # Photos button
        img10 = Image.open("Images/photos.jpg")
        img10 = img10.resize((195, 195), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        btn6.place(x=400, y=350, width=195, height=195)

        btn6_6 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn6_6.place(x=400, y=525, width=195, height=40)

        # Developer button
        img11 = Image.open("Images/developer.png")
        img11 = img11.resize((195, 195), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        btn7.place(x=700, y=350, width=195, height=195)

        btn7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn7_7.place(x=700, y=525, width=195, height=40)

        # Exit button
        img12 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((195, 195), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        btn8.place(x=1000, y=350, width=195, height=195)

        btn8_8 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn8_8.place(x=1000, y=525, width=195, height=40)

    def student_details(self):
     self.new_window = Toplevel(self.root)
     self.app = Student(self.new_window)



if __name__ == "__main__":
    main()
    # root= Tk()
    # app=login_window(root)
    # root.mainloop()
