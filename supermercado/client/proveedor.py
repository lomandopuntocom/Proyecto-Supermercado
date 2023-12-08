from tkinter import *
from model.supermercado_queries import *

class proveedorClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Market Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg = "white")
        self.root.focus_force()
        #=====Variables===
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_contacto=StringVar()
        self.var_direccion=StringVar() 
        #=====title===
        lbl_title= Label(self.root, text="Datos del Proveedor", font =("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        lbl_name= Label(self.root, text="Nombre:", font =("goudy old style", 18), bg="white").place(x=50, y =118)
        lbl_email= Label(self.root, text="Email:", font =("goudy old style", 18), bg="white").place(x=50, y =180)
        lbl_contacto= Label(self.root, text="Nro de Contacto:", font =("goudy old style", 18), bg="white").place(x=50, y =350)
        lbl_direccion= Label(self.root, text="Dirección:", font =("goudy old style", 18), bg="white").place(x=50, y =400)
        txt_name= Entry(self.root, textvariable=self.var_name, font =("goudy old style", 18), bg="white").place(x=230, y =120, width=300)
        txt_email= Entry(self.root, textvariable=self.var_email, font =("goudy old style", 18), bg="white").place(x=230, y =180, width=300)
        txt_contacto= Entry(self.root, textvariable=self.var_contacto, font =("goudy old style", 18), bg="white").place(x=230, y =350, width=300)        
        txt_direccion= Entry(self.root, textvariable=self.var_direccion, font =("goudy old style", 18), bg="white").place(x=230, y =400, width=300)        
        btn_add= Button(self.root, text="ADD",command= self.agregar_proveedor ,font =("goudy old style", 15), cursor="hand2").place(x=230, y =450, width=300, height=30)

    def agregar_proveedor(self):
        persona = PersonaDB(self.var_name.get(),  
                                self.var_email.get(), 
                                self.var_contacto.get(),
                                self.var_direccion.get())

        agregar_persona(persona)
        

if __name__=="__main__":
    root=Tk()
    obj=proveedorClass(root)
    root.mainloop()