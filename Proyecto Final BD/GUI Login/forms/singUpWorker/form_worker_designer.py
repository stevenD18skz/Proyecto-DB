import tkinter as tk
from tkinter import ttk
import util.generic as utl
from customtkinter import *
import tkinter.font as tkFont
import shutil
import os
from tkinter import messagebox


class FormRegisterWorkerDesigner():
    """clase encargada del diseño de la ventana registro de trabajador
    esta contiene todos los widgets necesario para la interfaz
    """
    def register():
        # Este método se encargará de registrar a un nuevo trabajador.
        pass

    """
    funcion para suabir una imagen a la aplicacion y guardar esta dentro de esta
    """
    def upload_image(self, destination_dir):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename:
            # Si se selecciona un archivo, se copia al directorio de destino.
            destination = os.path.join(destination_dir, os.path.basename(filename)).replace('\\', '/')
            shutil.copyfile(filename, destination)

            if "perfil" in destination_dir:
                 # Si el directorio de destino es para imágenes de perfil, se carga la imagen y se muestra en la interfaz.
                self.direccionPerfil = destination
                self.foto = utl.leer_imagen(destination, (220, 200))
                ola2 = tk.Label(self.frame_logo, image=self.foto, bg='#F87474', bd=0)
                ola2.place(x=61, y=65)

            else:
                # Si el directorio de destino es para otros documentos, se carga la imagen y se muestra en la interfaz.
                self.direccionDocumento = destination
                self.doc = utl.leer_imagen(destination, (200, 150))
                ola2 = tk.Label(self.frame_logo, image=self.doc, bg='#F87474', bd=0)
                ola2.place(x=71, y=318)

            



    """
    metodo contructor, contenedor de toda la parte de grafica de la ventana
    """
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('Resgitro de trabajador')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 820, 560)

        self.direccionPerfil = ""
        self.direccionDocumento = ""


        # ========================================> PANEL IZQUIERDA <====================================
        self.frame_logo = tk.Frame(self.ventana, bd=0, height=560, width = 342, padx=0, pady=0, bg='#fcfcfc')
        self.frame_logo.pack(side="left")
        etiqueta_usuario = tk.Label(
            master=self.frame_logo, 
            text="Registro trabajador", 
            font=('Exo', 24),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_usuario.place(x = 30, y = 5)

        

        imgPerfil = utl.leer_imagen("./resources/perfil.png", (220, 200))
        labelPerfil = tk.Label(self.frame_logo, image=imgPerfil, bg='#F87474', bd=0)
        labelPerfil.place(x=61, y=65)

        subirPerfil = CTkButton(
            master=self.frame_logo,
            text="Subir Foto",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=lambda: self.upload_image("./imagenesBD/perfilesTrabajador"), 
            width=200, 
            height=45
        )
        subirPerfil.place(x = 71, y = 268)
        subirPerfil.bind("<Return>", (lambda event: self.upload_image("./imagenesBD/perfilesTrabajador")))

        


        imgDocumento = utl.leer_imagen("./resources/documento.png", (200, 150))
        labelDocumento = tk.Label(self.frame_logo, image=imgDocumento, bg='#F87474', bd=0)
        labelDocumento.place(x=71, y=318)
        subirDocumento = CTkButton(
            master=self.frame_logo,
            text="Subir Documetno",
            corner_radius=32,
            font=('Exo', 15),
            text_color="#FFFFFF",
            border_width=0,
            fg_color="#689BFF",
            command=lambda: self.upload_image("./imagenesBD/documentosTrabajador"), 
            width=200, 
            height=45
        )
        subirDocumento.place(x = 71, y = 475)
        subirDocumento.bind("<Return>", (lambda event: self.upload_image("./imagenesBD/documentosTrabajador")))
        #self.frame_logo







        # ========================================> PANEL DERECHA <====================================
        frame_form = tk.Frame(self.ventana, bd=0,relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form
        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        variar = 115
        etiqueta_usuario = tk.Label(
            master=frame_form_fill, 
            text="Nombre", 
            font=('Exo', 16),
            fg="#000000", 
            bg='#fcfcfc', 
            anchor="w",
            height=2,
            padx=10
        )
        etiqueta_usuario.place(x = 0, y = variar + 10)
        self.entryUsuario = CTkEntry(
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
        self.entryUsuario.place(x = 135, y = variar + 10)

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
        etiqueta_apellido.place(x = 0, y = variar + 90)
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
        self.entryapellido.place(x = 135, y = variar + 90)



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
        etiqueta_documento.place(x = 0, y = variar + 170)
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
        self.entrydocumento.place(x = 135, y = variar + 170)



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
        etiqueta_direccion.place(x = 0, y = variar + 250)
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
        self.entrydireccion.place(x = 135, y = variar + 250)




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
        # end frame_form_fill



        self.ventana.mainloop()


