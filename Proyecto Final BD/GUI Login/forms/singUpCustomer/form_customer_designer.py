import tkinter as tk
from tkinter import ttk
import util.generic as utl
from customtkinter import *
import shutil
import os

class FormRegisterDesigner():
    def register():
        pass


    def upload_image(self, destination_dir):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename:
            destination = os.path.join(destination_dir, os.path.basename(filename)).replace('\\', '/')
            shutil.copyfile(filename, destination)
            self.direccionRecibo = destination
            self.foto = utl.leer_imagen(destination, (220, 150))
            ola2 = tk.Label(self.frame_logo, image=self.foto, bg='#F87474', bd=0)
            ola2.place(x= 40, y= 105)




    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Registro de cliente')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 820, 560)
        self.direccionRecibo = ""


        #frame_derecha
        self.frame_logo = tk.Frame(self.ventana, bd=0, height=560, width = 337,relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        self.frame_logo.pack(side="left")
        etiqueta_usuario = tk.Label(
            master=self.frame_logo, 
            text="Registro cliente", 
            font=('Exo', 24),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_usuario.place(x = 30, y = 20)




        imgRecibo = utl.leer_imagen("./resources/talonario-de-cheques.png", (220, 150))
        labelRecibo = tk.Label(self.frame_logo, image=imgRecibo, bg='#fcfcfc', bd=0)
        labelRecibo.place(x= 40, y= 105)
        cargar_recibo = CTkButton(
            master=self.frame_logo,
            text="Cargar recibo",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=lambda: self.upload_image("./imagenesBD/recibosClientes"),  
            width=200, 
            height=45
        )
        cargar_recibo.place(x = 50, y = 270)
        cargar_recibo.bind("<Return>", (lambda event: self.upload_image("./imagenesBD/recibosClientes")))



        imgTarjeta = utl.leer_imagen("./resources/tarjeta-de-credito.png", (220, 100))
        labelTarjeta = tk.Label(self.frame_logo, image=imgTarjeta, bg='#fcfcfc', bd=0)
        labelTarjeta.place(x= 25, y= 330)
        etiqueta_selecciona = tk.Label(
            master=self.frame_logo, 
            text="Selecciona tu medio de pago", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_selecciona.place(x = 5, y = 430)


        self.medio_pago = CTkComboBox(
            master=self.frame_logo, 
            values=["Credito", "Debito"], 
            font=('Exo', 16),
            fg_color="#689BFF", 
            border_color="#000000", 
            dropdown_fg_color="#0093E9"
        )
        self.medio_pago.place(x=60, y=480)



        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top

        # frame_izquierda
        frame_form_fill = tk.Frame(frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        variar = 20
        etiqueta_nombre = tk.Label(
            master=frame_form_fill, 
            text="Nombre", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_nombre.place(x = 0, y = variar + 10)
        self.entryNombre = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Nombre",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entryNombre.place(x = 135, y = variar + 10)



        etiqueta_apellido = tk.Label(
            master=frame_form_fill, 
            text="Apellido", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_apellido.place(x = 0, y = variar + 80)
        self.entryapellido = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Apellido",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entryapellido.place(x = 135, y = variar + 80)



        etiqueta_documento = tk.Label(
            master=frame_form_fill, 
            text="Documento", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_documento.place(x = 0, y = variar + 150)
        self.entrydocumento = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Documento",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entrydocumento.place(x = 135, y = variar + 150)



        etiqueta_correo = tk.Label(
            master=frame_form_fill, 
            text="Correo", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_correo.place(x = 0, y = variar + 220)
        self.entryCorreo = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Correo",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entryCorreo.place(x = 135, y = variar + 220)



        etiqueta_direccion = tk.Label(
            master=frame_form_fill, 
            text="Direccion", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_direccion.place(x = 0, y = variar + 290)
        self.entrydireccion = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Direccion",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entrydireccion.place(x = 135, y = variar + 290)



        etiqueta_celular = tk.Label(
            master=frame_form_fill, 
            text="Celular", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_celular.place(x = 0, y = variar + 360)
        self.entryCelular = CTkEntry(
            master=frame_form_fill,
            placeholder_text="Celular",
            corner_radius=62,
            border_width=0,
            font=('Exo', 17),
            text_color="#000000",
            fg_color="#DBE6FC",
            width=320, 
            height=57,
        )
        self.entryCelular.place(x = 135, y = variar + 360)



        
        registro = CTkButton(
            master=frame_form_fill,
            text="Registrar",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=self.register, 
            width=200, 
            height=45
        )
        registro.place(x = 255, y = 475)
        registro.bind("<Return>", (lambda event: self.register()))
        # end frame_izquierda
        # end frame_form_fill
        self.ventana.mainloop()

