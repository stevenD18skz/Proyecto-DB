import tkinter as tk
from tkinter import ttk
import util.generic as utl
from customtkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk, ImageDraw
import shutil
import os
import conexionDB
from tkinter import messagebox
import math
from tkinter import simpledialog
import datetime




class FormRContratoDesigner():

    # Define la función contratar con los parámetros self y posicion.
def contratar(self, posicion):
    # Selecciona el valor de la variable de búsqueda.
    seleccion = self.busqueda.get()
    # Consulta a la base de datos para obtener los datos de los trabajadores.
    datos_trabajadores = conexionDB.consultar(f"SELECT t.nombre, t.dir_gps, o.precio, t.calificacion, t.foto, t.id_trabajador FROM oferta as o NATURAL JOIN trabajador as t WHERE o.id_servicio = ( SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}')")
    # Consulta a la base de datos para obtener el número de celular del cliente.
    numero_celular = conexionDB.consultar(f"SELECT num_celular FROM CLIENTE WHERE usuario = '{self.usuario_cliente}'")
    # Prepara los datos del contrato.
    datos_contrato = [numero_celular[0][0], datos_trabajadores[(3*self.pagina) + posicion][5], 0]
    # Inserta los datos del contrato en la base de datos.
    conexionDB.insertar(datos_contrato, "CONTRATO")  

    # Pide al usuario que califique el trabajo.
    rating = simpledialog.askstring("Calificación", "¿Qué calificación le das al trabajador?")
    # Consulta a la base de datos para obtener el ID del contrato.
    id_contrato = conexionDB.consultar(f"SELECT * FROM contrato ORDER BY id_contrato DESC LIMIT 1;")[0][0]
    # Actualiza la calificación del contrato en la base de datos.
    conexionDB.update("contrato", "calificacion", rating, "id_contrato", id_contrato)
    
    # Consulta a la base de datos para calcular el nuevo promedio de calificaciones.
    nuevo_promedio = conexionDB.consultar(f"SELECT calcular_promedio('{datos_trabajadores[(3*self.pagina) + posicion][5]}');")
    # Actualiza la calificación del trabajador en la base de datos.
    conexionDB.update("trabajador", "calificacion", round(nuevo_promedio[0][0], 2), "id_trabajador", datos_trabajadores[(3*self.pagina) + posicion][5])

    # Prepara los datos del pago.
    datos_pago = []
    # Consulta a la base de datos para obtener el ID del servicio hecho.
    id_servicio_hecho = conexionDB.consultar(f"SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}'")[0][0]
    # Consulta a la base de datos para obtener el monto del pago.
    monto = conexionDB.consultar(f"select precio from oferta where id_trabajador = '{datos_trabajadores[(3*self.pagina) + posicion][5]}' and id_servicio = {id_servicio_hecho}")[0][0]
    # Agrega el monto al pago.
    datos_pago.append(monto)
    # Obtiene la fecha actual.
    fecha_actual = datetime.datetime.now()
    # Convierte la fecha a cadena.
    fecha_como_cadena = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    # Agrega la fecha al pago.
    datos_pago.append(fecha_como_cadena)
    # Agrega el número de celular al pago.
    datos_pago.append(numero_celular[0][0])
    # Agrega el ID del trabajador al pago.
    datos_pago.append(datos_trabajadores[(3*self.pagina) + posicion][5])
    # Muestra un mensaje con el monto del pago.
    messagebox.showinfo(message=f"Se le pagara al trabajador un total de {monto} dolares",title="Mensaje")
    # Inserta los datos del pago en la base de datos.
    conexionDB.insertar(datos_pago, "PAGO")






    # Define la función convertir_a_circular con los parámetros self, imagen y tamano.
def convertir_a_circular(self, imagen, tamano):
    # Abre la imagen proporcionada y la convierte a RGBA (Red, Green, Blue, Alpha).
    img = Image.open(imagen).convert("RGBA")
    # Redimensiona la imagen al tamaño proporcionado.
    img = img.resize(tamano)
    # Crea una nueva imagen RGBA con el tamaño proporcionado y un fondo transparente.
    fondo = Image.new('RGBA', tamano, (0, 0, 0, 0))
    # Crea un objeto de dibujo para el fondo.
    dibujo = ImageDraw.Draw(fondo)
    # Dibuja una elipse llena en el fondo que tiene el mismo tamaño que la imagen.
    dibujo.ellipse((0, 0, tamano[0], tamano[1]), fill=(255, 255, 255, 255))
    # Combina la imagen y el fondo utilizando la operación alpha_composite.
    img_circular = Image.alpha_composite(img, fondo)
    # Crea una nueva imagen en escala de grises con el tamaño proporcionado y un fondo negro.
    mascara = Image.new('L', tamano, 0)
    # Crea un objeto de dibujo para la máscara.
    dibujo = ImageDraw.Draw(mascara) 
    # Dibuja una elipse llena en la máscara que tiene el mismo tamaño que la imagen.
    dibujo.ellipse((0, 0, tamano[0], tamano[1]), fill=255)
    # Crea una nueva imagen RGBA con el tamaño proporcionado.
    img_circular = Image.new('RGBA', tamano)
    # Pega la imagen en la imagen circular utilizando la máscara.
    img_circular.paste(img, mask=mascara)
    # Devuelve la imagen circular.
    return img_circular

    # Define la función mostrar_seleccion con los parámetros self, event y sumador.
def mostrar_seleccion(self, event, sumador):
    # Selecciona el valor de la variable de búsqueda.
    seleccion = self.busqueda.get()
    # Consulta a la base de datos para obtener los datos de los trabajadores.
    datos_trabajadores = conexionDB.consultar(f"SELECT t.nombre, t.dir_gps, o.precio, t.calificacion, t.foto, t.id_trabajador FROM oferta as o NATURAL JOIN trabajador as t WHERE o.id_servicio = ( SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}') ORDER BY t.calificacion DESC, o.precio ASC")

    # Verifica si la página actual más el sumador es menor que 0.
    if self.pagina + sumador < 0:
        # Muestra un mensaje indicando que no hay páginas anteriores.
        messagebox.showinfo(message=f"ya no hay paginas anteriores",title="Mensaje") 
        return
            
    # Verifica si la página actual más el sumador multiplicado por 3 es mayor o igual que la longitud de los datos de los trabajadores.
    elif self.pagina+sumador*3 >= len(datos_trabajadores):#aqui es pa arriba
        # Muestra un mensaje indicando que no hay más trabajadores disponibles.
        messagebox.showinfo(message=f"ya no hay mas trabajadores disponible",title="Mensaje") 
        return

    # Si el sumador es 0, establece la página actual a 0.
    elif sumador == 0:
        self.pagina = 0

    # Si no, incrementa la página actual por el sumador.
    else:
        self.pagina += sumador

    # Define las etiquetas.
    etiquetas = [[self.foto1, self.etiqueta_nombre1, self.etiqueta_distancia1, self.etiqueta_precio1, self.etiqueta_calificacion1],
                [self.foto2, self.etiqueta_nombre2, self.etiqueta_distancia2, self.etiqueta_precio2, self.etiqueta_calificacion2],
                [self.foto3, self.etiqueta_nombre3, self.etiqueta_distancia3, self.etiqueta_precio3, self.etiqueta_calificacion3]]

    # Itera sobre el rango de 3.
    for i in range(3):
        try:
            # Convierte la foto del trabajador a una imagen circular.
            photo = self.convertir_a_circular(f"{datos_trabajadores[(3*self.pagina) + i][4]}", (100, 100))
            # Convierte la foto a un objeto PhotoImage de tkinter.
            img_tk = ImageTk.PhotoImage(photo)
            # Configura la imagen de la etiqueta.
            etiquetas[i][0].config(image=img_tk)
            etiquetas[i][0].image = img_tk
            # Configura el texto de la etiqueta del nombre.
            etiquetas[i][1].config(text = f"Nombre: {datos_trabajadores[(3*self.pagina) + i][0]}")
            # Consulta a la base de datos para calcular la distancia.
            diastancia = conexionDB.consultar(f"SELECT calculate_distance('{self.usuario_cliente}', '{datos_trabajadores[(3*self.pagina) + i][5]}') as distancia;")
            # Configura el texto de la etiqueta de la distancia.
            etiquetas[i][2].config(text = f"Distancia: {round(diastancia[0][0], 2)} km")#cambiar
            # Configura el texto de la etiqueta del precio.
            etiquetas[i][3].config(text = f"Precio: ${datos_trabajadores[(3*self.pagina) + i][2]}")
            # Configura el texto de la etiqueta de la calificación.
            etiquetas[i][4].config(text= f"Calificacion: {datos_trabajadores[(3*self.pagina) + i][3]}")
        except Exception as e: 
            # Si ocurre una excepción, configura las etiquetas con valores predeterminados.
            photo = self.convertir_a_circular("./resources/perfil.png", (100, 100))
            img_tk = ImageTk.PhotoImage(photo)
            etiquetas[i][0].config(image=img_tk)
            etiquetas[i][0].image = img_tk
            etiquetas[i][1].config(text = "Nombre: ------")
            etiquetas[i][2].config(text = "Distancia: ------")#cambiar
            etiquetas[i][3].config(text = "Precio: $------")
            etiquetas[i][4].config(text= "Calificacion: ------")







   # Define el método constructor __init__ con los parámetros self, parent e id_cliente.
def __init__(self, parent, id_cliente):  
    # Asigna el valor de id_cliente a la variable de instancia usuario_cliente.
    self.usuario_cliente = id_cliente    
    # Crea un nuevo marco (Frame) en el widget padre con un tamaño específico y un color de fondo.
    self.frame = tk.Frame(parent, width= 820, height = 560, bg = "#fcfcfc")
    # Inicializa la variable de instancia pagina a 0.
    self.pagina = 0
    # Consulta a la base de datos para obtener todos los servicios y guarda los nombres de los servicios en la lista valores.
    valores = list(map(lambda x: x[1], conexionDB.consultar("SELECT * FROM servicio")))
    # Crea una nueva etiqueta (Label) en el marco con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
    etiqueta_busqueda= tk.Label(
        master=self.frame, 
        text="Seleccionar servicio", 
        font=('Exo', 16),
        fg="#000000", 
        bg='#fcfcfc', 
        anchor="w",
        height=2,
        padx=10
    )
    # Coloca la etiqueta en una posición específica en el marco.
    etiqueta_busqueda.place(x = 50, y = 5) 
    # Crea un nuevo cuadro combinado (ComboBox) en el marco con los valores de la lista valores, una fuente, un color de texto, un color de borde, un color de texto desplegable y un comando que se ejecutará cuando se seleccione un elemento.
    self.busqueda = CTkComboBox(
        master=self.frame, 
        values=valores, 
        font=('Exo', 16),
        fg_color="#689BFF", 
        border_color="#000000", 
        dropdown_fg_color="#0093E9",
        command=lambda event: self.mostrar_seleccion(event, 0)
    )
    # Coloca el cuadro combinado en una posición específica en el marco.
    self.busqueda.place(x=260, y=20) 
    # Crea un nuevo botón (Button) en el marco con un texto específico, un radio de esquina, una fuente, un ancho de borde, un color de texto, un comando que se ejecutará cuando se haga clic en el botón, un ancho y una altura.
    self.anterior = CTkButton(
        master=self.frame,
        text="Anterior",
        corner_radius=32,
        font=('Exo', 11),
        border_width=0,
        fg_color="#689BFF",
        command=lambda: self.mostrar_seleccion(None, -1),
        width=80, 
        height=30
    )
    # Coloca el botón en una posición específica en el marco.
    self.anterior.place(x=640, y=525)  
    # Crea otro botón en el marco con las mismas características que el botón anterior pero con un texto y un comando diferentes.
    self.siguiente = CTkButton(
        master=self.frame,
        text="Siguiente",
        corner_radius=32,
        font=('Exo', 11),
        border_width=0,
        fg_color="#689BFF",
        command=lambda: self.mostrar_seleccion(None, 1),
        width=60, 
        height=30
    )
    # Coloca el botón en una posición específica en el marco.
    self.siguiente.place(x=730, y=525) 



        # ========================================> PANEL MEDIO <====================================
    # Crea un nuevo marco (Frame) en el marco self.frame con un tamaño específico, un color de primer plano y un radio de esquina.
    frame_logo = CTkFrame(self.frame, width=750, height=460, fg_color="#DBE6FC", corner_radius=32)
    # Coloca el marco en una posición específica en el marco self.frame.
    frame_logo.place(relx=.5, rely=.5, anchor="c", y=10)

    # Crea otro marco en el marco frame_logo con un tamaño específico, un color de primer plano y un radio de esquina.
    frame_perfil1 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
    # Coloca el marco en una posición específica en el marco frame_logo.
    frame_perfil1.place(relx=.5, rely=.5, anchor="c", y=-145)

    # Convierte la foto de perfil a una imagen circular.
    photo1 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
    # Convierte la foto a un objeto PhotoImage de tkinter.
    img_tk1 = ImageTk.PhotoImage(photo1)
    # Crea una nueva etiqueta (Label) en el marco frame_perfil1 con la imagen y un color de fondo.
    self.foto1 = tk.Label(frame_perfil1, image=img_tk1, bg = "#fcfcfc")
    # Guarda la imagen en la etiqueta.
    self.foto1.image = img_tk1 
    # Coloca la etiqueta en una posición específica en el marco frame_perfil1.
    self.foto1.place(x = 20, y = 15)

    # Crea una nueva etiqueta en el marco frame_perfil1 con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
    self.etiqueta_nombre1= tk.Label(
        master=frame_perfil1, 
        text="Nombre: ------", 
        font=('Exo', 16),
        fg="#000000", 
        bg='#fcfcfc', 
        anchor="w",
        height=2,
        padx=10
    )
    # Coloca la etiqueta en una posición específica en el marco frame_perfil1.
    self.etiqueta_nombre1.place(x = 125, y = 15)

    # Crea otra etiqueta en el marco frame_perfil1 con las mismas características que la etiqueta anterior pero con un texto diferente.
    self.etiqueta_calificacion1= tk.Label(
        master=frame_perfil1, 
        text="Calificacion: ------", 
        font=('Exo', 16),
        fg="#000000", 
        bg='#fcfcfc', 
        anchor="w",
        height=2,
        padx=10
    )
    # Coloca la etiqueta en una posición específica en el marco frame_perfil1.
    self.etiqueta_calificacion1.place(x = 125, y = 80)

# Crea otra etiqueta en el marco frame_perfil1 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_precio1= tk.Label(
    master=frame_perfil1, 
    text="Precio: $------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
    # Coloca la etiqueta en una posición específica en el marco frame_perfil1.
    self.etiqueta_precio1.place(x = 350, y=80)



# Crea una nueva etiqueta en el marco frame_perfil1 con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
self.etiqueta_distancia1= tk.Label(
    master=frame_perfil1, 
    text="Distancia: $------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil1.
self.etiqueta_distancia1.place(x = 350, y=15)

# Crea un nuevo botón en el marco frame_perfil1 con un texto específico, un radio de esquina, una fuente, un ancho de borde, un color de texto, un comando que se ejecutará cuando se haga clic en el botón, un ancho y una altura.
self.contratar1 = CTkButton(
    master=frame_perfil1,
    text="Contratar",
    corner_radius=32,
    font=('Exo', 11),
    border_width=0,
    fg_color="#7CA9FF",
    command=lambda: self.contratar(0),
    width=50, 
    height=50
)
# Coloca el botón en una posición específica en el marco frame_perfil1.
self.contratar1.place(x = 540,y = 70)

# Crea otro marco en el marco frame_logo con un tamaño específico, un color de primer plano y un radio de esquina.
frame_perfil2 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
# Coloca el marco en una posición específica en el marco frame_logo.
frame_perfil2.place(relx=.5, rely=.5, anchor="c", y=0)
# Convierte la foto de perfil a una imagen circular.
photo2 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
# Convierte la foto a un objeto PhotoImage de tkinter.
img_tk2 = ImageTk.PhotoImage(photo2)
# Crea una nueva etiqueta en el marco frame_perfil2 con la imagen y un color de fondo.
self.foto2 = tk.Label(frame_perfil2, image=img_tk2, bg = "#fcfcfc")
# Guarda la imagen en la etiqueta.
self.foto2.image = img_tk2
# Coloca la etiqueta en una posición específica en el marco frame_perfil2.
self.foto2.place(x = 20, y = 15)

# Crea una nueva etiqueta en el marco frame_perfil2 con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
self.etiqueta_nombre2= tk.Label(
    master=frame_perfil2, 
    text="Nombre: ------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil2.
self.etiqueta_nombre2.place(x = 125, y = 15)

# Crea otra etiqueta en el marco frame_perfil2 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_calificacion2= tk.Label(
    master=frame_perfil2, 
    text="Calificacion: ------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil2.
self.etiqueta_calificacion2.place(x = 125, y = 80)



# Crea una nueva etiqueta en el marco frame_perfil2 con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
self.etiqueta_precio2= tk.Label(
    master=frame_perfil2, 
    text="Precio: $------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil2.
self.etiqueta_precio2.place(x = 350, y=80)

# Crea otra etiqueta en el marco frame_perfil2 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_distancia2= tk.Label(
    master=frame_perfil2, 
    text="Distancia: $------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil2.
self.etiqueta_distancia2.place(x = 350, y=15)

# Crea un nuevo botón en el marco frame_perfil2 con un texto específico, un radio de esquina, una fuente, un ancho de borde, un color de texto, un comando que se ejecutará cuando se haga clic en el botón, un ancho y una altura.
self.contratar2 = CTkButton(
    master=frame_perfil2,
    text="Contratar",
    corner_radius=32,
    font=('Exo', 11),
    border_width=0,
    fg_color="#7CA9FF",
    command=lambda: self.contratar(1),
    width=50, 
    height=50
)
# Coloca el botón en una posición específica en el marco frame_perfil2.
self.contratar2.place(x = 540,y = 70) 

# Crea otro marco en el marco frame_logo con un tamaño específico, un color de primer plano y un radio de esquina.
frame_perfil3 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
# Coloca el marco en una posición específica en el marco frame_logo.
frame_perfil3.place(relx=.5, rely=.5, anchor="c", y=145)
# Convierte la foto de perfil a una imagen circular.
photo3 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
# Convierte la foto a un objeto PhotoImage de tkinter.
img_tk3 = ImageTk.PhotoImage(photo3)
# Crea una nueva etiqueta en el marco frame_perfil3 con la imagen y un color de fondo.
self.foto3 = tk.Label(frame_perfil3, image=img_tk3, bg = "#fcfcfc")
# Guarda la imagen en la etiqueta.
self.foto3.image = img_tk3
# Coloca la etiqueta en una posición específica en el marco frame_perfil3.
self.foto3.place(x = 20, y = 15)

# Crea una nueva etiqueta en el marco frame_perfil3 con un texto específico, una fuente, un color de texto, un color de fondo, una alineación, una altura y un relleno horizontal.
self.etiqueta_nombre3= tk.Label(
    master=frame_perfil3, 
    text="Nombre: ------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil3.
self.etiqueta_nombre3.place(x = 125, y = 15)

# Crea otra etiqueta en el marco frame_perfil3 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_calificacion3= tk.Label(
    master=frame_perfil3, 
    text="Calificacion: ------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil3.
self.etiqueta_calificacion3.place(x = 125, y = 80)  

# Crea otra etiqueta en el marco frame_perfil3 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_precio3= tk.Label(
    master=frame_perfil3, 
    text="Precio: $------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil3.
self.etiqueta_precio3.place(x = 350, y=80)

# Crea otra etiqueta en el marco frame_perfil3 con las mismas características que la etiqueta anterior pero con un texto diferente.
self.etiqueta_distancia3= tk.Label(
    master=frame_perfil3, 
    text="Distancia: ------", 
    font=('Exo', 16),
    fg="#000000", 
    bg='#fcfcfc', 
    anchor="w",
    height=2,
    padx=10
)
# Coloca la etiqueta en una posición específica en el marco frame_perfil3.
self.etiqueta_distancia3.place(x = 350, y=15)

# Crea un nuevo botón en el marco frame_perfil3 con un texto específico, un radio de esquina, una fuente, un ancho de borde, un color de texto, un comando que se ejecutará cuando se haga clic en el botón, un ancho y una altura.
self.contratar3 = CTkButton(
    master=frame_perfil3,
    text="Contratar",
    corner_radius=32,
    font=('Exo', 11),
    border_width=0,
    fg_color="#7CA9FF",
    command=lambda: self.contratar(2),
    width=50, 
    height=50
)
# Coloca el botón en una posición específica en el marco frame_perfil3.
self.contratar3.place(x = 540,y = 70)




