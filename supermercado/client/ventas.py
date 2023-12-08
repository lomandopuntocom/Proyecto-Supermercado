from tkinter import *
from model.supermercado_queries import *

class ventasClass:
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
        self.var_fecha=StringVar()
        self.var_monto=StringVar()
        self.var_metodo_pago=StringVar()
        #=====title===
        lbl_title= Label(self.root, text="Datos de Venta", font =("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        lbl_title_cliente= Label(self.root, text="Datos del Cliente:", font =("goudy old style", 22), fg="black").place(x=50, y=60)
        lbl_name= Label(self.root, text="Nombre:", font =("goudy old style", 18), bg="white").place(x=50, y =110)
        lbl_email= Label(self.root, text="Email:", font =("goudy old style", 18), bg="white").place(x=50, y =150)
        lbl_contacto= Label(self.root, text="Nro de Contacto:", font =("goudy old style", 18), bg="white").place(x=50, y =190)
        lbl_direccion= Label(self.root, text="Dirección:", font =("goudy old style", 18), bg="white").place(x=50, y =230)
        lbl_title_nota_venta= Label(self.root, text="Datos de la Venta:", font =("goudy old style", 22), fg="black").place(x=50, y=280)
        lbl_fecha= Label(self.root, text="Fecha emisión:", font =("goudy old style", 18), bg="white").place(x=50, y =330)
        lbl_monto= Label(self.root, text="Monto:", font =("goudy old style", 18), bg="white").place(x=50, y =370)
        lbl_metodo_pago= Label(self.root, text="Método de Pago:", font =("goudy old style", 18), bg="white").place(x=50, y =410)

        txt_name= Entry(self.root, textvariable=self.var_name, font =("goudy old style", 18), bg="white").place(x=230, y =110, width=300)
        txt_email= Entry(self.root, textvariable=self.var_email, font =("goudy old style", 18), bg="white").place(x=230, y =150, width=300)
        txt_contacto= Entry(self.root, textvariable=self.var_contacto, font =("goudy old style", 18), bg="white").place(x=230, y =190, width=300)        
        txt_direccion= Entry(self.root, textvariable=self.var_direccion, font =("goudy old style", 18), bg="white").place(x=230, y =230, width=300)        
        txt_fecha= Entry(self.root, textvariable=self.var_email, font =("goudy old style", 18), bg="white").place(x=230, y =330, width=300)
        txt_monto= Entry(self.root, textvariable=self.var_contacto, font =("goudy old style", 18), bg="white").place(x=230, y =370, width=300)        
        txt_metodo_pago= Entry(self.root, textvariable=self.var_direccion, font =("goudy old style", 18), bg="white").place(x=230, y =410, width=300)        
        btn_add= Button(self.root, text="ADD",command= self.agregar_proveedor ,font =("goudy old style", 15), cursor="hand2").place(x=230, y =450, width=300, height=30)

    def agregar_ventas(self):
        ventas = VentasDB(self.var_name.get(),  
                                self.var_email.get(), 
                                self.var_contacto.get(),
                                self.var_direccion.get(),
                                self.var_fecha.get(),
                                self.var_monto.get(),
                                self.var_metodo_pago.get())

        agregar_ventas(ventas)
        

if __name__=="__main__":
    root=Tk()
    obj=ventasClass(root)
    root.mainloop()