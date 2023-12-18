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




class FormPerfilTrabajadorDesigner():

    def editar(self):
        pass

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


    def __init__(self, nombre_usuario):
        datos_trabajador = (conexionDB.consultar(f"SELECT * FROM TRABAJADOR WHERE id_trabajador = '{nombre_usuario}'"))[0]
        self.ventana = tk.Toplevel()
        self.ventana.title('Perfil Usuario')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 820, 560)


        self.frame_app_main = tk.Frame(self.ventana, bd=0, width=420,relief=tk.SOLID, padx=0, pady=0, bg='#fcfcfc')
        self.frame_app_main.pack(expand=tk.YES, fill=tk.BOTH)


        # frame_logo
        frame_logo = tk.Frame(self.frame_app_main, bd=0, height=560, width=300,relief=tk.SOLID, padx=0, pady=0, bg='#689BFF')
        frame_logo.place(x=0, y=0)


        photo = self.convertir_a_circular(f"{datos_trabajador[2]}", (215, 215))
        img_tk = ImageTk.PhotoImage(photo)
        self.foto = tk.Label(frame_logo, image=img_tk, bg = "#689BFF")
        self.foto.image = img_tk
        self.foto.place(x = 50, y = 70)


        self.etiqueta_nombre= CTkLabel(
            master=frame_logo, 
            text=f"Nombre: {datos_trabajador[6]} {datos_trabajador[7]}", 
            font=('Exo', 16), 
            corner_radius=32,
            fg_color="#fcfcfc",
            text_color= "#000000",
            anchor="center", 
            justify="center",
            height=40,
            padx=10
        )

        self.etiqueta_nombre.place(x = 10, y = 350)


        self.etiqueta_calificacion= CTkLabel(
            master=frame_logo, 
            text=f"Calificacion: {datos_trabajador[9]}", 
            font=('Exo', 16),
            corner_radius=32,
            fg_color="#fcfcfc",
            text_color= "#000000", 
            anchor="center", 
            justify="center",
            height=40,
            padx=10
        )
        self.etiqueta_calificacion.place(x = 10, y = 400)


        self.etiqueta_estado= CTkLabel(
            master=frame_logo, 
            text=f"Estado: libre", 
            font=('Exo', 16),
            corner_radius=32,
            fg_color="#fcfcfc",
            text_color= "#000000", 
            anchor="center", 
            justify="center",
            height=40,
            padx=10
        )
        self.etiqueta_estado.place(x = 10, y = 450)


        # frame_form
        frame_form = tk.Frame(self.frame_app_main, bd=0, height=560, width=900, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.place(x=300, y=0)


        etiqueta_mis_labores = tk.Label(
            master=frame_form, 
            text="Mis labores", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_mis_labores.place(x = 40, y = 20)


        




        editar = CTkButton(
            master=frame_form,
            text="Editar",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=lambda: self.editar(nombre_usuario), 
            width=200, 
            height=45
        )
        editar.place(x = 290, y = 500)


        # frame_form_fill
        frame_form_fill = CTkFrame(
            master=frame_form,
            width=460,
            height=400,
            border_width=0,
            corner_radius=30,
            fg_color="#DBE6FC"
        )
        #azul
        frame_form_fill.place(x=30, y=80)


        etiqueta_labor = tk.Label(
            master=frame_form_fill, 
            text="Labor", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#DBE6FC', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_labor.place(x = 40, y = 20)


        etiqueta_costo = tk.Label(
            master=frame_form_fill, 
            text="Costo", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#DBE6FC', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_costo.place(x = 350, y = 20)



        datos_labores = conexionDB.consultar(f"SELECT s.nombre, precio  FROM oferta  NATURAL JOIN servicio s WHERE id_trabajador = '{nombre_usuario}'")
        lab = ""
        for i in datos_labores:
            lab += f"\n{i[0].ljust(35)} ${i[1]}"


        self.poner_labores = tk.Label(
            master=frame_form_fill, 
            text=lab, 
            font=('Exo', 14),
            fg="#000000", 
            bg='#DBE6FC', 
            anchor="w",
            height=len(datos_labores)+3,
            padx=0,
            pady=0
        )
        self.poner_labores.place(x = 30, y = 60)

        self.ventana.mainloop()