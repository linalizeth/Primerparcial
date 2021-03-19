CREATE TABLE productos(
    id                  INT(11) NOT NULL AUTO_INCREMENT,
    nombre              VARCHAR(255) NOT NULL,
    descripcion         VARCHAR(255),
    precio_venta        FLOAT(14, 2) NOT NULL,
    precio_compra       FLOAT(14, 2) NOT NULL,
    porcentaje_ganacia  FLOAT(5, 2) NOT NULL,
    estado              BOOLEAN,
    CONSTRAINT pk_productos PRIMARY KEY(id)
);