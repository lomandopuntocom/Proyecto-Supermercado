# Market Manager

## Descargo de Responsabilidad
Este proyecto aplica conceptos de programación y base de datos para fines educativos, utilizando Python y una base de datos Oracle. Se centra en la programación orientada a objetos y el formato snake_case para la base de datos.

## Introducción
Market Manager es un programa diseñado para facilitar la administración de una base de datos de supermercado. Permite la gestión eficiente de inventarios, clientes, proveedores y ventas, incluyendo la capacidad de realizar consultas, añadir productos, categorías, clientes y proveedores a la base de datos.

## Estructura de Base de Datos
- **Tabla Categoría:** Gestiona las categorías de productos.
- **Tabla Producto:** Almacena información de productos y se relaciona con las tablas `proveedor` y `categoría`.
- **Tabla Inventario:** Registra existencias de productos.
- **Tabla Persona:** Contiene información sobre individuos asociados al supermercado.
- **Tabla Proveedor y Cliente:** Define roles de personas como proveedores o clientes.
- **Tabla Nota_Venta y Detalle_Venta:** Maneja detalles de transacciones de venta.
- **Tabla Factura:** Almacena información de facturas generadas.

## Funciones del Programa
- Añadir nuevas categorías y productos.
- Gestión de personas y su asignación a clases específicas.
- Consultas a tablas específicas y de ventas recientes.

## Fases del Desarrollo
- Diseño del diagrama de clases.
- Configuración de la base de datos en Oracle.
- Conexión de la base de datos a Python.
- Diseño e implementación de la interfaz de usuario con Tkinter.

## Previsualización de la Interfaz
![Interfaz Inicial](images/main.jpg)
![Categorias](images/categoria.jpg)
![Productos](images/producto.jpg)
![Proveedor](images/proveedor.jpg)

## Licencia
'OracleDB'
'Tkinter'