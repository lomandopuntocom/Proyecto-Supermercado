from random import randint, choice, uniform
from datetime import datetime, timedelta
import pandas as pd

# Number of entries to create
num_entries = 100

# Helper functions
def random_date(start, end):
    """Generate a random datetime between start and end"""
    return start + timedelta(
        # Get a random amount of seconds between start and end
        seconds=randint(0, int((end - start).total_seconds())),
    )

def random_string(prefix, length=10):
    """Generate a random string of fixed length """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return prefix + ''.join(choice(letters) for i in range(length - len(prefix)))

# Generate data for each table
# Persona
personas = [{"id": i, 
             "nombre": random_string("Person_"), 
             "email": f"email_{i}@example.com", 
             "num_contacto": randint(100000000, 999999999), 
             "direccion": random_string("Address_", 20)} for i in range(1, num_entries + 1)]

# Proveedor
proveedores = [{"id": i, "id_persona": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Categoria
categorias = [{"id": i, 
               "nombre": random_string("Category_"), 
               "descripcion": random_string("Desc_", 50),
               "id_categoria_principal": randint(1, num_entries) if i > 1 else None} for i in range(1, num_entries + 1)]

# Producto
productos = [{"id": i, 
              "nombre": random_string("Product_"), 
              "descripcion": random_string("Desc_", 50),
              "precio": round(uniform(10.0, 1000.0), 2),
              "id_proveedor": randint(1, num_entries),
              "id_categoria": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Inventario
inventarios = [{"id": i, 
                "stock": randint(0, 500),
                "fecha_ingreso": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)),
                "id_producto": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Cliente
clientes = [{"id": i, "id_persona": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Nota de Venta
nota_ventas = [{"id": i,
                "fecha": random_date(datetime(2021, 1, 1), datetime(2023, 1, 1)),
                "monto": round(uniform(50.0, 5000.0), 2),
                "metodo_pago": choice(["Efectivo", "Tarjeta", "Transferencia"]),
                "id_cliente": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Detalle Venta
detalle_ventas = [{"id": i, 
                   "cantidad": randint(1, 10),
                   "precio": round(uniform(10.0, 1000.0), 2),
                   "id_producto": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Factura
facturas = [{"nro_factura": i,
             "nit": randint(100000000, 999999999),
             "cod_auth": randint(100000, 999999),
             "descripcion": random_string("Factura_", 50),
             "id_nota_venta": randint(1, num_entries)} for i in range(1, num_entries + 1)]

# Convert to DataFrames for better display
df_personas = pd.DataFrame(personas)
df_proveedores = pd.DataFrame(proveedores)
df_categorias = pd.DataFrame(categorias)
df_productos = pd.DataFrame(productos)
df_inventarios = pd.DataFrame(inventarios)
df_clientes = pd.DataFrame(clientes)
df_nota_ventas = pd.DataFrame(nota_ventas)
df_detalle_ventas = pd.DataFrame(detalle_ventas)
df_facturas = pd.DataFrame(facturas)

df_personas.head(), df_proveedores.head(), df_categorias.head(), df_productos.head(), df_inventarios.head(), df_clientes.head(), df_nota_ventas.head(), df_detalle_ventas.head(), df_facturas.head()



