# Importa la clase FormEditarPerfilTrabajadorDesigner desde el módulo forms.editar_perfil_trabajador.form_editar_perfil_trabajador_designer.
from forms.editar_perfil_trabajador.form_editar_perfil_trabajador_designer import FormEditarPerfilTrabajadorDesigner
# Importa el módulo messagebox desde tkinter.
from tkinter import messagebox
# Importa el módulo tkinter como tk.
import tkinter as tk 
# Importa el módulo conexionDB.
import conexionDB

# Define la clase FormEditarPerfilTrabajador que hereda de FormEditarPerfilTrabajadorDesigner.
class FormEditarPerfilTrabajador(FormEditarPerfilTrabajadorDesigner):
    # Define el método constructor __init__ con los parámetros self y nombre_usuario.
    def __init__(self, nombre_usuario):
        # Llama al método constructor de la clase padre con el parámetro nombre_usuario.
        super().__init__(nombre_usuario)
