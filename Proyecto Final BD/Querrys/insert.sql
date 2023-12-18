INSERT INTO SERVICIO (nombre) VALUES
('Jardineria'),
('Limpieza'),
('Vigilancia'),
('Cuidado de niños'),
('Cuidado de mascotas'),
('Lavado de autos'),
('Mantenimiento de piscinas'),
('Electricista'),
('Fontaneria'),
('Mudanza');


INSERT INTO TRABAJADOR (foto, imagen_documento, dir_gps, direccion, nombre, apellido, documento, calificacion) VALUES
('./imagenesBD/perfilesTrabajador/perfil1.JPG', 'doc1.jpg', '4.6097102,-74.081749', 'Calle 45 #20-30, Cali', 'Sara', 'Pérez', '123456789', 4.3),
('./imagenesBD/perfilesTrabajador/perfil2.JPG', 'doc2.jpg', '3.4517927,-76.5324943', 'Carrera 66 #11-24, Cali', 'María', 'Rodríguez', '987654321',3.0),
('./imagenesBD/perfilesTrabajador/perfil3.JPG', 'doc3.jpg', '6.2443382,-75.573553', 'Calle 70 #52-45, Cali', 'Carlos', 'González', '112233445', 4.1),
('./imagenesBD/perfilesTrabajador/perfil4.JPG', 'doc4.jpg', '10.9685401,-74.7813187', 'Carrera 38 #74-56, Yumbo', 'Angela', 'Martínez', '556677889', 3.5),
('./imagenesBD/perfilesTrabajador/perfil5.JPG', 'doc5.jpg', '4.6482837,-74.2478903', 'Avenida 68 #26-50, Cali', 'Pedro', 'Gómez', '998877665', 4.5);



INSERT INTO OFERTA (id_trabajador, id_servicio, precio) VALUES
('SA1000P-123', 1, 150),
('MA1110R-987', 2, 180),
('CA1220G-112', 3, 110),
('AN1330M-556', 4, 120),
('PE1440G-998', 5, 130);

INSERT INTO OFERTA (id_trabajador, id_servicio, precio) VALUES
('SA1000P-123', 6, 150),
('MA1110R-987', 7, 180),
('CA1220G-112', 8, 110),
('AN1330M-556', 9, 120),
('PE1440G-998', 10, 130);


INSERT INTO OFERTA (id_trabajador, id_servicio, precio) VALUES
('SA1000P-123', 10, 150),
('MA1110R-987', 9, 180),
('CA1220G-112', 8, 110),
('AN1330M-556', 7, 120),
('PE1440G-998', 6, 130);

INSERT INTO OFERTA (id_trabajador, id_servicio, precio) VALUES
('SA1000P-123', 5, 150),
('MA1110R-987', 4, 180),
('CA1220G-112', 3, 110),
('AN1330M-556', 2, 120),
('PE1440G-998', 1, 130);


INSERT INTO CLIENTE (num_celular, email, medio_pago, nombre, apellido, documento, direccion, dir_gps, recibo) VALUES
(3001234567, 'andres@gmail.com', 'Tarjeta de crédito', 'Andrés', 'Martínez', '1234567890', 'Calle 123 #45-67', '3.451647,-76.532494', 'Recibo1'),
(3002345678, 'sofia@gmail.com', 'Tarjeta de débito', 'Sofía', 'López', '2345678901', 'Carrera 89 #10-20', '3.452647,-76.533494', 'Recibo2'),
(3003456789, 'gabriel@gmail.com', 'Tarjeta de débito', 'Gabriel', 'Torres', '3456789012', 'Avenida 6N #23-34', '3.453647,-76.534494', 'Recibo3'),
(3004567890, 'isabella@gmail.com', 'Tarjeta de crédito', 'Isabella', 'Ramírez', '4567890123', 'Calle 70 #30-40', '3.454647,-76.535494', 'Recibo4'),
(3005678901, 'santiago@gmail.com', 'Tarjeta de débito', 'Santiago', 'Gutiérrez', '5678901234', 'Carrera 33 #56-78', '3.455647,-76.536494', 'Recibo5');




INSERT INTO CONTRATO (num_celular_cliente, id_trabajador, calificacion) VALUES
(3001234567, 'SA1000P-123', 4.5),
(3002345678, 'MA1110R-987', 3.7),
(3003456789, 'CA1220G-112', 4.2),
(3004567890, 'AN1330M-556', 5.0),
(3005678901, 'PE1440G-998', 4.8);


INSERT INTO PAGO (monto, fecha, num_celular_cliente, id_trabajador) VALUES
('50000', '2023-01-01', 3001234567, 'SA1000P-123'),
('60000', '2023-02-01', 3002345678, 'MA1110R-987'),
('70000', '2023-03-01', 3003456789, 'CA1220G-112'),
('80000', '2023-04-01', 3004567890, 'AN1330M-556'),
('90000', '2023-05-01', 3005678901, 'PE1440G-998');