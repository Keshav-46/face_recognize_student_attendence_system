from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Registration Form')
        self.root.geometry("1600x500+0+0")




#object ko open garna
if __name__ == "__main__":
   root= Tk()
   app=Register(root)
   root.mainloop()  