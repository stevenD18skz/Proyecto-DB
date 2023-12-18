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

    def contratar(self, posicion):
        #contratar
        seleccion = self.busqueda.get()
        datos_trabajadores = conexionDB.consultar(f"SELECT t.nombre, t.dir_gps, o.precio, t.calificacion, t.foto, t.id_trabajador FROM oferta as o NATURAL JOIN trabajador as t WHERE o.id_servicio = ( SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}')")
        numero_celular = conexionDB.consultar(f"SELECT num_celular FROM CLIENTE WHERE usuario = '{self.usuario_cliente}'")
        datos_contrato = [numero_celular[0][0], datos_trabajadores[(3*self.pagina) + posicion][5], 0]
        conexionDB.insertar(datos_contrato, "CONTRATO")  

        #calificar trabajo
        rating = simpledialog.askstring("Calificación", "¿Qué calificación le das al trabajador?")
        id_contrato = conexionDB.consultar(f"SELECT * FROM contrato ORDER BY id_contrato DESC LIMIT 1;")[0][0]
        conexionDB.update("contrato", "calificacion", rating, "id_contrato", id_contrato)
        

        #caztualizar promedio
        nuevo_promedio = conexionDB.consultar(f"SELECT calcular_promedio('{datos_trabajadores[(3*self.pagina) + posicion][5]}');")
        conexionDB.update("trabajador", "calificacion", round(nuevo_promedio[0][0], 2), "id_trabajador", datos_trabajadores[(3*self.pagina) + posicion][5])

        #pagar
        datos_pago = []
        id_servicio_hecho = conexionDB.consultar(f"SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}'")[0][0]
        monto = conexionDB.consultar(f"select precio from oferta where id_trabajador = '{datos_trabajadores[(3*self.pagina) + posicion][5]}' and id_servicio = {id_servicio_hecho}")[0][0]
        datos_pago.append(monto)
        fecha_actual = datetime.datetime.now()
        fecha_como_cadena = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        datos_pago.append(fecha_como_cadena)
        datos_pago.append(numero_celular[0][0])
        datos_pago.append(datos_trabajadores[(3*self.pagina) + posicion][5])
        messagebox.showinfo(message=f"Se le pagara al trabajador un total de {monto} dolares",title="Mensaje")
        conexionDB.insertar(datos_pago, "PAGO")






    def convertir_a_circular(self, imagen, tamano):
        img = Image.open(imagen).convert("RGBA")
        img = img.resize(tamano)
        fondo = Image.new('RGBA', tamano, (0, 0, 0, 0))
        dibujo = ImageDraw.Draw(fondo)
        dibujo.ellipse((0, 0, tamano[0], tamano[1]), fill=(255, 255, 255, 255))
        img_circular = Image.alpha_composite(img, fondo)
        mascara = Image.new('L', tamano, 0)
        dibujo = ImageDraw.Draw(mascara) 
        dibujo.ellipse((0, 0, tamano[0], tamano[1]), fill=255)
        img_circular = Image.new('RGBA', tamano)
        img_circular.paste(img, mask=mascara)
        return img_circular


    def mostrar_seleccion(self, event, sumador):
        seleccion = self.busqueda.get()
        datos_trabajadores = conexionDB.consultar(f"SELECT t.nombre, t.dir_gps, o.precio, t.calificacion, t.foto, t.id_trabajador FROM oferta as o NATURAL JOIN trabajador as t WHERE o.id_servicio = ( SELECT id_servicio FROM servicio WHERE nombre = '{seleccion}') ORDER BY t.calificacion DESC, o.precio ASC")

        if self.pagina + sumador < 0:
            messagebox.showinfo(message=f"ya no hay paginas anteriores",title="Mensaje") 
            return
            
        elif self.pagina+sumador*3 >= len(datos_trabajadores):#aqui es pa arriba
            messagebox.showinfo(message=f"ya no hay mas trabajadores disponible",title="Mensaje") 
            return

        elif sumador == 0:
            self.pagina = 0

        else:
            self.pagina += sumador


        etiquetas = [[self.foto1, self.etiqueta_nombre1, self.etiqueta_distancia1, self.etiqueta_precio1, self.etiqueta_calificacion1],
                [self.foto2, self.etiqueta_nombre2, self.etiqueta_distancia2, self.etiqueta_precio2, self.etiqueta_calificacion2],
                [self.foto3, self.etiqueta_nombre3, self.etiqueta_distancia3, self.etiqueta_precio3, self.etiqueta_calificacion3]]


        for i in range(3):
            try:
                photo = self.convertir_a_circular(f"{datos_trabajadores[(3*self.pagina) + i][4]}", (100, 100))
                img_tk = ImageTk.PhotoImage(photo)
                etiquetas[i][0].config(image=img_tk)
                etiquetas[i][0].image = img_tk
                etiquetas[i][1].config(text = f"Nombre: {datos_trabajadores[(3*self.pagina) + i][0]}")
                diastancia = conexionDB.consultar(f"SELECT calculate_distance('{self.usuario_cliente}', '{datos_trabajadores[(3*self.pagina) + i][5]}') as distancia;")
                etiquetas[i][2].config(text = f"Distancia: {round(diastancia[0][0], 2)} km")#cambiar
                etiquetas[i][3].config(text = f"Precio: ${datos_trabajadores[(3*self.pagina) + i][2]}")
                etiquetas[i][4].config(text= f"Calificacion: {datos_trabajadores[(3*self.pagina) + i][3]}")
            except Exception as e: 
                photo = self.convertir_a_circular("./resources/perfil.png", (100, 100))
                img_tk = ImageTk.PhotoImage(photo)
                etiquetas[i][0].config(image=img_tk)
                etiquetas[i][0].image = img_tk
                etiquetas[i][1].config(text = "Nombre: ------")
                etiquetas[i][2].config(text = "Distancia: ------")#cambiar
                etiquetas[i][3].config(text = "Precio: $------")
                etiquetas[i][4].config(text= "Calificacion: ------")






    def __init__(self, parent, id_cliente):  
        self.usuario_cliente = id_cliente    
        self.frame = tk.Frame(parent, width= 820, height = 560, bg = "#fcfcfc")
        self. pagina = 0
        valores = list(map(lambda x: x[1], conexionDB.consultar("SELECT * FROM servicio")))
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
        etiqueta_busqueda.place(x = 50, y = 5)

        self.busqueda = CTkComboBox(
            master=self.frame, 
            values=valores, 
            font=('Exo', 16),
            fg_color="#689BFF", 
            border_color="#000000", 
            dropdown_fg_color="#0093E9",
            command=lambda event: self.mostrar_seleccion(event, 0)
        )
        self.busqueda.place(x=260, y=20)



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
        self.anterior.place(x=640, y=525)

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
        self.siguiente.place(x=730, y=525)



        


        







        




        # ========================================> PANEL MEDIO <====================================
        frame_logo = CTkFrame(self.frame, width=750, height=460, fg_color="#DBE6FC", corner_radius=32)
        frame_logo.place(relx=.5, rely=.5, anchor="c", y=10)




        frame_perfil1 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
        frame_perfil1.place(relx=.5, rely=.5, anchor="c", y=-145)


        

        photo1 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
        img_tk1 = ImageTk.PhotoImage(photo1)
        self.foto1 = tk.Label(frame_perfil1, image=img_tk1, bg = "#fcfcfc")
        self.foto1.image = img_tk1 
        self.foto1.place(x = 20, y = 15)


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
        self.etiqueta_nombre1.place(x = 125, y = 15)


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
        self.etiqueta_calificacion1.place(x = 125, y = 80)


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
        self.etiqueta_precio1.place(x = 350, y=80)


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
        self.etiqueta_distancia1.place(x = 350, y=15)

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
        self.contratar1.place(x = 540,y = 70)

        





        frame_perfil2 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
        frame_perfil2.place(relx=.5, rely=.5, anchor="c", y=0)
        photo2 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
        img_tk2 = ImageTk.PhotoImage(photo2)
        self.foto2 = tk.Label(frame_perfil2, image=img_tk2, bg = "#fcfcfc")
        self.foto2.image = img_tk2
        self.foto2.place(x = 20, y = 15)


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
        self.etiqueta_nombre2.place(x = 125, y = 15)


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
        self.etiqueta_calificacion2.place(x = 125, y = 80)


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
        self.etiqueta_precio2.place(x = 350, y=80)


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
        self.etiqueta_distancia2.place(x = 350, y=15)

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
        self.contratar2.place(x = 540,y = 70)






        frame_perfil3 = CTkFrame(frame_logo, width=650, height=135, fg_color="#fcfcfc", corner_radius=32)
        frame_perfil3.place(relx=.5, rely=.5, anchor="c", y=145)
        photo3 = self.convertir_a_circular("./resources/perfil.png", (100, 100))
        img_tk3 = ImageTk.PhotoImage(photo3)
        self.foto3 = tk.Label(frame_perfil3, image=img_tk3, bg = "#fcfcfc")
        self.foto3.image = img_tk3
        self.foto3.place(x = 20, y = 15)

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
        self.etiqueta_nombre3.place(x = 125, y = 15)

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
        self.etiqueta_calificacion3.place(x = 125, y = 80)

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
        self.etiqueta_precio3.place(x = 350, y=80)


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
        self.etiqueta_distancia3.place(x = 350, y=15)

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
        self.contratar3.place(x = 540,y = 70)



