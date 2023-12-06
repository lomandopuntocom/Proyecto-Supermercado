from tkinter import *
from client.category import categoryClass
class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Market Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")
        # TITLE
        head = Label(root, text='Market Management System', font=('times new roman', 30, 'bold'), bg='Red', fg='white', bd=10, relief = RIDGE).pack(fill =X)
        btn_category = Button(text='Category',command=self.category,  padx=20, pady=10, font=('times new roman', 20, 'bold'))
        btn_category.place(relx=0.04, rely=0.4, anchor="w")

        btn_product = Button(text='Products', padx=20, pady=10, font=('times new roman', 20, 'bold'))
        btn_product.place(relx=0.04, rely=0.6, anchor="w")

        btn_product = Button(text='Supplier', padx=20, pady=10, font=('times new roman', 20, 'bold'))
        btn_product.place(relx=0.04, rely=0.8 , anchor="w")

    def category(self):
        self.new_win= Toplevel(self.root)
        self.new_obj= categoryClass(self.new_win)


