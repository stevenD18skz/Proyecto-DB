from forms.editar_perfil_trabajador.form_editar_perfil_trabajador_designer import FormEditarPerfilTrabajadorDesigner
from tkinter import messagebox
import tkinter as tk 
import conexionDB



class FormEditarPerfilTrabajador(FormEditarPerfilTrabajadorDesigner):
    def __init__(self, nombre_usuario):
        super().__init__(nombre_usuario)