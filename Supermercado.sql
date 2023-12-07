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

select * from persona;

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

