from forms.perfil_trabajador.form_perfil_trabajador_designer import FormPerfilTrabajadorDesigner
from forms.editar_perfil_trabajador.form_editar_perfil_trabajador import FormEditarPerfilTrabajadorDesigner
from tkinter import messagebox
import tkinter as tk 
import conexionDB



class FormPerfilTrabajador(FormPerfilTrabajadorDesigner):
    def __init__(self, nombre_usuario):
        super().__init__(nombre_usuario)

    def editar(self, nombre_usuario):
        FormEditarPerfilTrabajadorDesigner(nombre_usuario)

