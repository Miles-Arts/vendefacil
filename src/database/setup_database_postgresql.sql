-- Script de creación de tablas para PostgreSQL
-- Tablas: id_personas y productos

CREATE TABLE id_personas (
    documento INT NOT NULL PRIMARY KEY,
    nombres CHAR(250) NOT NULL,
    apellidos CHAR(250) NOT NULL,
    correo VARCHAR(250) NOT NULL,
    metodo_de_pago INT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    celular VARCHAR(250) NOT NULL
);

CREATE TABLE productos (
    id_producto INT NOT NULL PRIMARY KEY,
    categoria_producto INT NOT NULL,
    id_compra FLOAT NOT NULL,
    caracteristicas_producto VARCHAR(250) NOT NULL,
    tipo_producto INT NOT NULL,
    tamaño_producto INT NOT NULL,
    precio_producto FLOAT NOT NULL,
    mes_del_producto INT NOT NULL,
    nombre_producto VARCHAR(250) NOT NULL
);
