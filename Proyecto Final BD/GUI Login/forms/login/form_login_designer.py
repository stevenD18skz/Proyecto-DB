import tkinter as tk
import util.generic as utl
from customtkinter import *
import os



class FormLoginDesigner():

    def verificar(self):
        pass
    
    def userRegister(self):
        pass

    def workerRegister(self):
        pass

    

    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('820x560')
        self.ventana.config(bg='yellow')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 820, 560)

        self.frame_app_main = tk.Frame(self.ventana, bd=0, width=420,relief=tk.SOLID, padx=0, pady=0, bg='#FFFFFF')
        self.frame_app_main.pack(expand=tk.YES, fill=tk.BOTH)

    
        # frame_logo
        frame_logo = tk.Frame(self.frame_app_main, bd=0, width=420,relief=tk.SOLID, padx=0, pady=0, bg='#FFFFFF')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        nombre = tk.Label(frame_logo, text="DomesticApp", font=('Exo', 32), fg="#000000", bg='#FFFFFF')
        nombre.place(x=55, y=60)
        descripcion = tk.Label(frame_logo, text="Una plataforma para la contratación de servicios domésticos", font=('Exo', 10), fg="#000000", bg='#FFFFFF')
        descripcion.place(x=55, y=105)
        logo = utl.leer_imagen("./resources/backLogIn.png", (425, 420))
        label = tk.Label(frame_logo, image=logo, bg='#FFFFFF', bd = 0)
        label.place(x=0, y=180)

        # frame_form
        frame_form = tk.Frame(self.frame_app_main, bd=0, relief=tk.SOLID, bg='#FFFFFF')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_fill
        frame_form_fill = CTkFrame(
            master=frame_form,
            width=350,
            height=415,
            border_width=0,
            corner_radius=68,
            fg_color="#92C7F9"
        )
        #azul
        frame_form_fill.pack(side="bottom", expand=tk.YES)

        title = tk.Label(frame_form_fill, text="Inicio sesion", font=('Exo', 28), fg="white", bg='#92C7F9')
        title.place(x = 70, y = 20)
        self.entryUsuario = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Nombre De Usuario",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="white",
            width=300, 
            height=46,
        )
        self.entryUsuario.place(x=25, y=90)

        #self.password.config(show="*")
        self.entryPassword = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Contraseña",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="white",
            width=300, 
            height=46,
        )
        self.entryPassword.configure(show="*")
        self.entryPassword.place(x=25, y=153)




        btnInicio = CTkButton(
            master=frame_form_fill,
            text="Iniciar Sesion",
            corner_radius=32,
            font=('Exo', 14),
            border_width=0,
            fg_color="#689BFF",
            command=self.verificar, 
            width=80, 
            height=50
        )
        btnInicio.place(x=100, y=215)
        btnInicio.bind("<Return>", (lambda event: self.verificar()))




        pregunta = tk.Label(frame_form_fill, text="¿Aún no tienes una cuenta?", font=('Exo', 10), fg="#000000", bg='#92C7F9')
        pregunta.place(x = 90, y = 270)

        btnRegistroC = CTkButton(
            master=frame_form_fill,
            text="Crear cuenta\ntrabajador",
            corner_radius=32,
            font=('Exo', 14),
            border_width=0,
            fg_color="#689BFF",
            command=self.workerRegister, 
            width=80, 
            height=50
        )
        btnRegistroC.place(x=30, y=310)
        btnRegistroC.bind("<Return>", (lambda event: self.workerRegister()))


        btnRegistroW = CTkButton(
            master=frame_form_fill,
            text="Crear cuenta\ncliente",
            corner_radius=32,
            font=('Exo', 14),
            border_width=0,
            fg_color="#689BFF",
            command=self.userRegister, 
            width=80, 
            height=50
        )
        btnRegistroW.place(x=175, y=310)
        btnRegistroW.bind("<Return>", (lambda event: self.userRegister()))


        
        # end frame_form_fill
        self.ventana.mainloop()
