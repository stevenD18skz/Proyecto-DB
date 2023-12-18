CREATE TABLE CLIENTE (
    num_celular VARCHAR(500) NOT NULL PRIMARY KEY,
	usuario VARCHAR(500) NOT NULL,
	pass_word VARCHAR(500) NOT NULL,
    email VARCHAR(500) NOT NULL,
    medio_pago VARCHAR(500) NOT NULL,
    nombre VARCHAR(500) NOT NULL,
    apellido VARCHAR(500) NOT NULL,
    documento VARCHAR(500) NOT NULL,
    direccion VARCHAR(500) NOT NULL,
    dir_gps VARCHAR(500) NOT NULL,
    recibo VARCHAR(500) NOT NULL
);

CREATE SEQUENCE sec_cliente
START WITH 1000
INCREMENT BY 110;


-- Crear la tabla TRABAJADOR
CREATE TABLE TRABAJADOR (
    id_trabajador VARCHAR(500) NOT NULL PRIMARY KEY,
	pass_word VARCHAR(500) NOT NULL,
    foto VARCHAR(500) NOT NULL,
    imagen_documento VARCHAR(500) NOT NULL,
    dir_gps VARCHAR(500) NOT NULL,
    direccion VARCHAR(500) NOT NULL,
    nombre VARCHAR(500) NOT NULL,
    apellido VARCHAR(500) NOT NULL,
    documento VARCHAR(500) NOT NULL,
	calificacion DOUBLE PRECISION
);

-- Crear la secuencia sec_trabajador
CREATE SEQUENCE sec_trabajador
START WITH 1000
INCREMENT BY 110;


CREATE TABLE SERVICIO (
    id_servicio SERIAL PRIMARY KEY,
    nombre VARCHAR(500) 
);


CREATE TABLE OFERTA (
    id_oferta SERIAL PRIMARY KEY,
    id_trabajador VARCHAR(500),
    id_servicio INT,
    precio INT,
    FOREIGN KEY (id_trabajador) REFERENCES TRABAJADOR(id_trabajador)  ON DELETE CASCADE,
    FOREIGN KEY (id_servicio) REFERENCES SERVICIO(id_servicio)  ON DELETE CASCADE
);



CREATE TABLE CONTRATO (
    id_contrato SERIAL PRIMARY KEY NOT NULL,
    num_celular_cliente VARCHAR(500)NOT NULL,
    id_trabajador VARCHAR(500) NOT NULL,
    calificacion DOUBLE PRECISION,
	FOREIGN KEY (num_celular_cliente) REFERENCES CLIENTE(num_celular),
	FOREIGN KEY (id_trabajador) REFERENCES TRABAJADOR(id_trabajador)
);



CREATE TABLE PAGO (
    id_pago SERIAL PRIMARY KEY NOT NULL,
    monto VARCHAR(500) NOT NULL,
    fecha DATE NOT NULL,
    num_celular_cliente VARCHAR(500) NOT NULL,
    id_trabajador VARCHAR(500) NOT NULL,
    FOREIGN KEY (num_celular_cliente) REFERENCES CLIENTE(num_celular),
    FOREIGN KEY (id_trabajador) REFERENCES TRABAJADOR(id_trabajador)
);





