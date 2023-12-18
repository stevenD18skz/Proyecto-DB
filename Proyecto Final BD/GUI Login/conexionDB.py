import psycopg2

try:
    #se crea la conexion con la base de datos
    conexion = psycopg2.connect(
        host="localhost",
        database="Proyecto-DB",
        user="postgres",
        password="1234"
    )
    print("Conexión exitosa")
    cursor = conexion.cursor()

    #funcion para hacer una consulta
    def consultar(string):
        consulta_sql = string
        cursor.execute(consulta_sql)
        consulta_usuario = cursor.fetchall()
        return consulta_usuario

    #funcion para insertar un dato en alguna tabla
    def insertar(lista, tabla):
        columnas = {
            "TRABAJADOR": "(foto, imagen_documento, dir_gps, direccion, nombre, apellido, documento, calificacion)",
            "CLIENTE": "(num_celular, email, medio_pago, nombre, apellido, documento, direccion, dir_gps, recibo)",
            "CONTRATO":"(num_celular_cliente, id_trabajador, calificacion)",
            "OFERTA": "(id_trabajador, id_servicio, precio)",
            "PAGO": "(monto, fecha, num_celular_cliente, id_trabajador)"}

        insertar_sql = f"Insert into {tabla} {columnas[tabla]} values {tuple(lista)}"
        cursor.execute(insertar_sql)
        conexion.commit()

    #funcion para actualizar un elemento
    def update(tabla, columa, valor, identificador, id_valor):
        update_sql = f"UPDATE {tabla} SET {columa} = {valor} WHERE {identificador} = '{id_valor}'"
        cursor.execute(update_sql)
        conexion.commit()
        


except Exception as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)