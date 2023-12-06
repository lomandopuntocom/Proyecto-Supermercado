from tkinter import *

class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Market Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg = "white")
        self.root.focus_force()
        #=====Variables===
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        self.var_desc=StringVar()
        #=====title===
        lbl_title= Label(self.root, text="Manage Product Category", font =("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        lbl_name= Label(self.root, text="Category Name:", font =("goudy old style", 18), bg="white").place(x=50, y =118)
        lbl_description= Label(self.root, text="Description:", font =("goudy old style", 18), bg="white").place(x=50, y =198)
        txt_name= Entry(self.root, textvariable=self.var_name, font =("goudy old style", 18), bg="white").place(x=230, y =120, width=300)
        txt_description= Entry(self.root, textvariable=self.var_desc, font =("goudy old style", 18), bg="white").place(x=230, y =200, width=300, height = 140)
        btn_add= Button(self.root, text="ADD", font =("goudy old style", 15), cursor="hand2").place(x=230, y =350, width=150, height=30)

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop() 