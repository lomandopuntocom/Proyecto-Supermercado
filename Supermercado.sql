create table categoria (
	"id" int not null primary key,
	nombre varchar(100) not null,
	descripcion varchar(200) not null,
	id_categoria_principal int,
	constraint fk_categoria_principal foreign key (id_categoria_principal) references categoria("id")
);
create sequence categoria_sec start with 1 increment by 1;

create table persona (
	"id" int not null primary key,
	nombre varchar(100) not null,
	email varchar(100) not null,
	num_contacto int,
	direccion varchar(200) not null
);
create sequence persona_sec start with 1 increment by 1;

delete from cliente;

select * from persona

create table proveedor (
	"id" int not null primary key,
	id_persona int not null,
	constraint fk_persona_proveedor foreign key (id_persona) references persona("id")
);
create sequence proveedor_sec start with 1 increment by 1;

create table producto(
	"id" int not null primary key,
	nombre varchar(100) not null,
	descripcion varchar(200) not null,
	precio number not null,
	id_proveedor int,
	id_categoria int,
	constraint fk_producto_proveedor foreign key (id_proveedor) references proveedor("id"),
	constraint fk_producto_categoria foreign key (id_categoria) references categoria("id")
);
create sequence producto_sec start with 1 increment by 1;

create table inventario (
	"id" int not null primary key,
	stock int not null,
	fecha_ingreso date not null,
	id_producto int not null,
	constraint fk_producto_inventario foreign key (id_producto) references producto("id")
);
create sequence inventario_sec start with 1 increment by 1;

create table cliente (
	"id" int not null primary key,
	id_persona int,
	constraint fk_persona_cliente foreign key (id_persona) references persona("id")
);
create sequence cliente_sec start with 1 increment by 1;

create table nota_venta (
	"id" int not null primary key,
	fecha date not null,
	monto number not null,
	metodo_pago varchar(100) not null,
	id_cliente int,
	constraint fk_cliente_nota_venta foreign key (id_cliente) references cliente("id")
);
create sequence nota_venta_sec start with 1 increment by 1;

create table detalle_venta (
	"id" int not null primary key,
	cantidad int not null,
	id_producto int,
	constraint fk_producto_detalle_venta foreign key (id_producto) references producto("id"),
	id_nota_venta int,
	constraint fk_nota_venta_detalle_venta foreign key (id_nota_venta) references nota_venta("id")
);
create sequence detalle_venta_sec start with 1 increment by 1;

create table factura (
	nro_factura int not null primary key,
	nit int,
	cod_auth int not null,
	descripcion varchar(200) not null,
	id_nota_venta int not null,
	constraint fk_nota_venta_factura foreign key (id_nota_venta) references nota_venta("id")
);
create sequence factura_sec start with 1 increment by 1;













-- Poblar categorias
DECLARE
  i INT;
BEGIN
  FOR i IN 1..20 LOOP
    INSERT INTO categoria ("id", nombre, descripcion)
    VALUES (categoria_sec.NEXTVAL, 'Categoria ' || i, 'Descripción de Categoria ' || i);

    -- Subcategorias
    INSERT INTO categoria ("id", nombre, descripcion, id_categoria_principal)
    VALUES (categoria_sec.NEXTVAL, 'Subcategoria ' || (i*2-1), 'Descripción de Subcategoria ' || (i*2-1), categoria_sec.CURRVAL - 1);
    INSERT INTO categoria ("id", nombre, descripcion, id_categoria_principal)
    VALUES (categoria_sec.NEXTVAL, 'Subcategoria ' || (i*2), 'Descripción de Subcategoria ' || (i*2), categoria_sec.CURRVAL - 1);
  END LOOP;
END;
/

select * from cliente
-- Poblar personas
BEGIN
  FOR i IN 1..100 LOOP
    INSERT INTO persona ("id", nombre, email, num_contacto, direccion)
    VALUES (persona_sec.NEXTVAL, 'Persona ' || i, 'email' || i || '@example.com', DBMS_RANDOM.VALUE(10000000,99999999), 'Dirección ' || i);
  END LOOP;
END;
/

-- Poblar proveedores y clientes
DECLARE
  personas_id DBMS_SQL.NUMBER_TABLE;
BEGIN
  -- Obtener los IDs de la tabla persona
  SELECT "id" BULK COLLECT INTO personas_id FROM persona;

  -- Poblar proveedores
  FOR i IN 1..20 LOOP
    INSERT INTO proveedor ("id", id_persona)
    VALUES (proveedor_sec.NEXTVAL, personas_id(i));
  END LOOP;

  -- Poblar clientes
  FOR i IN 21..personas_id.COUNT LOOP
    INSERT INTO cliente ("id", id_persona)
    VALUES (cliente_sec.NEXTVAL, personas_id(i));
  END LOOP;
END;
/


-- Poblar productos e inventario
BEGIN
  FOR i IN 1..60 LOOP
    -- Seleccionar un id_proveedor al azar para cada producto
    INSERT INTO producto ("id", nombre, descripcion, precio, id_proveedor, id_categoria)
    SELECT producto_sec.NEXTVAL, 'Producto ' || i, 'Descripción de Producto ' || i, DBMS_RANDOM.VALUE(10, 100), 
           (SELECT "id" FROM (SELECT "id" FROM proveedor ORDER BY DBMS_RANDOM.VALUE) WHERE ROWNUM = 1), 
           DBMS_RANDOM.VALUE(1, 60)
    FROM dual;

    -- Insertar en inventario
    INSERT INTO inventario ("id", stock, fecha_ingreso, id_producto)
    VALUES (inventario_sec.NEXTVAL, DBMS_RANDOM.VALUE(20, 100), SYSDATE, producto_sec.CURRVAL);
  END LOOP;
END;
/

select * from inventario

-- Poblar notas de venta, detalles y facturas
DECLARE
  num_ventas INT;
  cliente_id INT;
  producto_id INT;
BEGIN
  FOR i IN (SELECT "id" FROM cliente) LOOP
    cliente_id := i."id";
    num_ventas := DBMS_RANDOM.VALUE(1, 3);

    FOR j IN 1..num_ventas LOOP
      INSERT INTO nota_venta ("id", fecha, monto, metodo_pago, id_cliente)
      VALUES (nota_venta_sec.NEXTVAL, SYSDATE, DBMS_RANDOM.VALUE(100, 1000), 'Efectivo', cliente_id);

      -- Seleccionar un id_producto al azar para cada detalle de venta
      SELECT "id" INTO producto_id FROM (SELECT "id" FROM producto ORDER BY DBMS_RANDOM.VALUE) WHERE ROWNUM = 1;

      INSERT INTO detalle_venta ("id", cantidad, id_producto, id_nota_venta)
      VALUES (detalle_venta_sec.NEXTVAL, DBMS_RANDOM.VALUE(1, 10), producto_id, nota_venta_sec.CURRVAL);

      INSERT INTO factura (nro_factura, nit, cod_auth, descripcion, id_nota_venta)
      VALUES (factura_sec.NEXTVAL, DBMS_RANDOM.VALUE(1000000,9999999), DBMS_RANDOM.VALUE(100000,999999), 'Factura de venta', nota_venta_sec.CURRVAL);
    END LOOP;
  END LOOP;
END;
/

select * from factura