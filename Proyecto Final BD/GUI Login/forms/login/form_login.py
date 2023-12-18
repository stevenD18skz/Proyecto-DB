from tkinter import messagebox
from forms.login.form_login_designer import FormLoginDesigner
import conexionDB
import time
from tkinter import *


from forms.singUpWorker.form_worker import FormWorker
from forms.singUpCustomer.form_customer import FormCustomer
from forms.contrato.form_contrato import FormContrato
from forms.perfil_trabajador.form_perfil_trabajador import FormPerfilTrabajador



class FormLogin(FormLoginDesigner):
    """
    Esta clase se encarga de manejar la funcionalidad de inicio de sesión de la aplicación.
    Hereda de la clase FormLoginDesigner.
    """

    def __init__(self):
        """
        Método constructor. Llama al constructor de la superclase.
        """
        super().__init__()

    def verificar(self):
        """
        Este método verifica las credenciales del usuario.
        Primero verifica si el usuario es un trabajador, si no lo es, verifica si el usuario es un cliente.
        Si se encuentra al usuario y la contraseña coincide, da la bienvenida al usuario y abre el formulario correspondiente.
        Si la contraseña no coincide o el usuario no existe, muestra un mensaje de error.
        """
        nombreUsuario = self.entryUsuario.get()
        password = self.entryPassword.get()

        usuario = conexionDB.consultar(f"SELECT id_trabajador, pass_word, nombre, apellido FROM TRABAJADOR WHERE id_trabajador = '{nombreUsuario}';")
        tipo_usuario = "T"

        if len(usuario) == 0:
            usuario = conexionDB.consultar(f"SELECT usuario, pass_word, nombre, apellido  FROM cliente WHERE usuario = '{nombreUsuario}';")
            tipo_usuario = "C"

        if len(usuario) == 1:
            if password == usuario[0][1]:
                messagebox.showinfo(message=f"Bienvenido a DomesticApp {usuario[0][2]} {usuario[0][3]}",title="Mensaje")

                if tipo_usuario == "T":
                    self.ventana.iconify()
                    FormPerfilTrabajador(usuario[0][0])

                else:
                    form_contrato = FormContrato(self.frame_app_main, usuario[0][0])
                    form_contrato.frame.pack(side = "left")
                    self.ventana.title("Pagina de contratacion")
                    all_widgets = self.frame_app_main.winfo_children()
                    for widget in all_widgets:
                        if widget != form_contrato.frame:
                            widget.destroy()

            else:
                messagebox.showerror(message="contraseña incorrecta",title="Mensaje")  
                self.entryPassword.delete(0, 'end')

        else:
            messagebox.showerror(message="tu usuario no existe",title="Mensaje")  
            self.entryUsuario.delete(0, 'end')

    def userRegister(self):
        """
        Este método se utiliza para registrar un nuevo usuario.
        Abre el formulario FormCustomer.
        """
        self.ventana.iconify()
        FormCustomer()

    def workerRegister(self):
        """
        Este método se utiliza para registrar un nuevo trabajador.
        Abre el formulario FormWorker.
        """
        self.ventana.iconify()
        FormWorker()
