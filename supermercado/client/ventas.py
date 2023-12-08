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
        self.var_cantidad=StringVar()
        self.var_id_producto=StringVar()
        #=====title===
        lbl_title= Label(self.root, text="Datos de Venta", font =("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        lbl_title_cliente= Label(self.root, text="Datos del Cliente:", font =("goudy old style", 22), fg="black").place(x=50, y=60)
        lbl_name= Label(self.root, text="Nombre:", font =("goudy old style", 18), bg="white").place(x=50, y =110)
        lbl_email= Label(self.root, text="Email:", font =("goudy old style", 18), bg="white").place(x=50, y =150)
        lbl_contacto= Label(self.root, text="Nro de Contacto:", font =("goudy old style", 18), bg="white").place(x=50, y =190)
        lbl_direccion= Label(self.root, text="Dirección:", font =("goudy old style", 18), bg="white").place(x=50, y =230)
        lbl_title_nota_venta= Label(self.root, text="Datos de la Venta:", font =("goudy old style", 22), fg="black").place(x=50, y=320)
        lbl_fecha= Label(self.root, text="Fecha emisión:", font =("goudy old style", 18), bg="white").place(x=50, y =380)
        lbl_monto= Label(self.root, text="Monto Total:", font =("goudy old style", 18), bg="white").place(x=50, y =420)
        lbl_metodo_pago= Label(self.root, text="Método de Pago:", font =("goudy old style", 18), bg="white").place(x=50, y =460)
        lbl_title_detalle_venta= Label(self.root, text="Detalle Venta:", font =("goudy old style", 22), fg="black").place(x=550, y=60)
        lbl_cantidad= Label(self.root, text="Cantidad:", font =("goudy old style", 18), bg="white").place(x=550, y =110)
        lbl_id_producto= Label(self.root, text="ID del producto:", font =("goudy old style", 18), bg="white").place(x=550, y =150)
        
        txt_name= Entry(self.root, textvariable=self.var_name, font =("goudy old style", 18), bg="white").place(x=230, y =110, width=300)
        txt_email= Entry(self.root, textvariable=self.var_email, font =("goudy old style", 18), bg="white").place(x=230, y =150, width=300)
        txt_contacto= Entry(self.root, textvariable=self.var_contacto, font =("goudy old style", 18), bg="white").place(x=230, y =190, width=300)        
        txt_direccion= Entry(self.root, textvariable=self.var_direccion, font =("goudy old style", 18), bg="white").place(x=230, y =230, width=300)        
        txt_fecha= Entry(self.root, textvariable=self.var_fecha, font =("goudy old style", 18), bg="white").place(x=230, y =380, width=300)
        txt_monto= Entry(self.root, textvariable=self.var_monto, font =("goudy old style", 18), bg="white").place(x=230, y =420, width=300)        
        txt_metodo_pago= Entry(self.root, textvariable=self.var_metodo_pago, font =("goudy old style", 18), bg="white").place(x=230, y =460, width=300)        
        txt_cantidad= Entry(self.root, textvariable=self.var_cantidad, font =("goudy old style", 18), bg="white").place(x=750, y =110, width=240)
        txt_id_producto= Entry(self.root, textvariable=self.var_id_producto, font =("goudy old style", 18), bg="white").place(x=750, y =150, width=240)
        btn_add= Button(self.root, text="ADD",command= self.agregar_cliente ,font =("goudy old style", 15), cursor="hand2").place(x=230, y =280, width=300, height=30)
        btn_add2= Button(self.root, text="ADD",command= self.agregar_nota_venta ,font =("goudy old style", 15), cursor="hand2").place(x=550, y =380, width=50, height=110)
        btn_add3= Button(self.root, text="ADD",command= self.agregar_detalle_venta ,font =("goudy old style", 15), cursor="hand2").place(x=1005, y =105, width=50, height=75)

    def agregar_cliente(self):
        persona = PersonaDB(self.var_name.get(),  
                                self.var_email.get(), 
                                self.var_contacto.get(),
                                self.var_direccion.get())

        agregar_persona2(persona)

    def agregar_nota_venta(self):
        nota_venta = Nota_VentaDB(self.var_fecha.get(),  
                                self.var_monto.get(), 
                                self.var_metodo_pago.get())

        agregar_nota_venta(nota_venta)

    def agregar_detalle_venta(self):
        detalle_venta = Detalle_VentaDB(self.var_cantidad.get(),  
                                self.var_id_producto.get())

        agregar_detalle_venta(detalle_venta)
        

if __name__=="__main__":
    root=Tk()
    obj=ventasClass(root)
    root.mainloop()