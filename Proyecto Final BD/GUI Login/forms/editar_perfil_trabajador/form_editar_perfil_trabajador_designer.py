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




class FormEditarPerfilTrabajadorDesigner():
    def agregar_labor(self, nombre_usuario):
        # Esta función se encarga de agregar una nueva labor para un trabajador.
        datos_oferta = [nombre_usuario]
        id_servicio = conexionDB.consultar(f"SELECT id_servicio from servicio where nombre = '{self.seleccionar_labores.get().capitalize()}'")
        datos_oferta.append(id_servicio[0][0])
        datos_oferta.append(self.entry_precio.get())
        cant = conexionDB.consultar(f"select count(id_servicio) from oferta where id_trabajador = '{nombre_usuario}' and id_servicio = {id_servicio[0][0]}")

        # Aquí se verifica si la labor ya existe para el trabajador.
        if cant[0][0] == 0:
            # Si la labor no existe, se inserta en la base de datos.
            conexionDB.insertar(datos_oferta, "OFERTA")
            messagebox.showinfo(message=f"Tu nueva labor se inserto con exito",title="Mensaje")
            self.ventana.destroy()

        else:
            # Si la labor ya existe, se actualiza el precio en la base de datos.
            conexionDB.update("OFERTA", "precio", self.entry_precio.get(), "id_servicio", id_servicio[0][0])
            messagebox.showinfo(message=f"el precio por tu labor se actualizo con extio",title="Mensaje")
            self.ventana.destroy()

    #Este es el constructor de la parte visual
    def __init__(self, nombre_usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title('Perfil Usuario')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 400)


        self.frame_app_main = tk.Frame(self.ventana, bd=0, width=420,relief=tk.SOLID, padx=0, pady=0, bg='#DBE6FC')
        self.frame_app_main.pack(expand=tk.YES, fill=tk.BOTH)


        etiqueta_editar = tk.Label(
            master=self.frame_app_main, 
            text="Edita tu perfil", 
            font=('Exo', 20),
            fg="#000000", 
            bg='#DBE6FC', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_editar.place(x = 30, y = 15)


        self.etiqueta_selecciona= CTkLabel(
            master=self.frame_app_main, 
            text="Selecciona tu labor", 
            font=('Exo', 16), 
            corner_radius=32,
            fg_color="#689BFF",
            text_color= "#fcfcfc",
            anchor="center", 
            justify="center",
            height=40,
            padx=10
        )

        self.etiqueta_selecciona.place(x = 30, y = 90)

        valores = list(map(lambda x: x[1], conexionDB.consultar("SELECT * FROM servicio")))
        self.seleccionar_labores = CTkComboBox(
            master=self.frame_app_main, 
            values=valores, 
            font=('Exo', 16),
            fg_color="#689BFF", 
            border_color="#000000", 
            dropdown_fg_color="#0093E9"
        )
        self.seleccionar_labores.place(x=300, y=95)


        self.etiqueta_precio= CTkLabel(
            master=self.frame_app_main, 
            text="Precio", 
            font=('Exo', 16), 
            corner_radius=32,
            fg_color="#689BFF",
            text_color= "#fcfcfc",
            anchor="center", 
            justify="center",
            height=40,
            padx=10
        )

        self.etiqueta_precio.place(x = 30, y = 200)


        self.entry_precio = CTkEntry(
            master=self.frame_app_main,
            placeholder_text="Precio",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#fcfcfc",
            width=320, 
            height=57,
        )
        self.entry_precio.place(x = 300, y = 185)


        guardar = CTkButton(
            master=self.frame_app_main,
            text="Guardar",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=lambda: self.agregar_labor(nombre_usuario), 
            width=200, 
            height=45
        )
        guardar.place(x = 290, y = 315)

        self.ventana.mainloop()
