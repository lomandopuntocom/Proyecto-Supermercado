from tkinter import *
from model.supermercado_queries import *

class productClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Market Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg = "white")
        self.root.focus_force()
        #=====Variables===
        self.var_name=StringVar()
        self.var_desc=StringVar()
        self.var_precio=StringVar()
        self.var_id_categoria=StringVar()
        self.var_id_proveedor=StringVar()
        #=====title===
        lbl_title= Label(self.root, text="Manage Product Category", font =("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        lbl_name= Label(self.root, text="Product Name:", font =("goudy old style", 18), bg="white").place(x=50, y =118)
        lbl_description= Label(self.root, text="Description:", font =("goudy old style", 18), bg="white").place(x=50, y =180)
        lbl_precio= Label(self.root, text="Precio:", font =("goudy old style", 18), bg="white").place(x=50, y =350)
        lbl_id_proveedor= Label(self.root, text="ID Proveedor:", font =("goudy old style", 18), bg="white").place(x=50, y =400)
        lbl_id_categoria= Label(self.root, text="ID Categoría:", font =("goudy old style", 18), bg="white").place(x=305, y =400)
        txt_name= Entry(self.root, textvariable=self.var_name, font =("goudy old style", 18), bg="white").place(x=230, y =120, width=300)
        txt_description= Entry(self.root, textvariable=self.var_desc, font =("goudy old style", 18), bg="white").place(x=230, y =180, width=300, height = 140)
        txt_precio= Entry(self.root, textvariable=self.var_precio, font =("goudy old style", 18), bg="white").place(x=230, y =350, width=300)        
        txt_id_proveedor= Entry(self.root, textvariable=self.var_id_proveedor, font =("goudy old style", 18), bg="white").place(x=230, y =400, width=60)        
        txt_id_categoria= Entry(self.root, textvariable=self.var_id_categoria, font =("goudy old style", 18), bg="white").place(x=450, y =400, width=80)        
        btn_add= Button(self.root, text="ADD",command= self.agregar_producto ,font =("goudy old style", 15), cursor="hand2").place(x=230, y =450, width=300, height=30)

    def agregar_producto(self):
        # Lógica para agregar la categoría
        producto = ProductoDB(self.var_name.get(),  
                                self.var_desc.get(),
                                self.var_precio.get(),
                                self.var_id_proveedor(),
                                self.var_id_categoria())
        agregar_precio(producto)

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()