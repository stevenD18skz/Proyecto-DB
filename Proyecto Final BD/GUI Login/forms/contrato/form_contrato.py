# Importa la clase FormRContratoDesigner desde el módulo form_contrato_designer 
# que se encuentra en el paquete forms.contrato.
from forms.contrato.form_contrato_designer import FormRContratoDesigner

# Importa el módulo messagebox de la biblioteca tkinter. 
# Este módulo se utiliza para mostrar cuadros de mensaje.
from tkinter import messagebox

# Importa la biblioteca tkinter como tk. 
# tkinter es una biblioteca de Python para crear interfaces gráficas de usuario.
import tkinter as tk 

# Importa el módulo conexionDB. 
# Este módulo probablemente se utiliza para interactuar con una base de datos.
import conexionDB

# Aquí se define la clase FormContrato que hereda de la clase FormRContratoDesigner.
class FormContrato(FormRContratoDesigner):
    # El método __init__ es el constructor de la clase.
    def __init__(self, parent, id_cliente):
        # La función super() se utiliza para llamar a un método en una clase padre. 
        # En este caso, se está llamando al constructor de la clase FormRContratoDesigner.
        super().__init__(parent, id_cliente)
