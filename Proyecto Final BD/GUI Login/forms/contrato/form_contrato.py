from forms.contrato.form_contrato_designer import FormRContratoDesigner
from tkinter import messagebox
import tkinter as tk 
import conexionDB


class FormContrato(FormRContratoDesigner):
    def __init__(self, parent, id_cliente):
        super().__init__(parent, id_cliente)