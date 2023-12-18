from forms.singUpCustomer.form_customer_designer import FormRegisterDesigner
from tkinter import messagebox
import tkinter as tk
import conexionDB
from geopy.geocoders import Nominatim
import psycopg2




class FormCustomer(FormRegisterDesigner):
    def __init__(self):
        super().__init__()


    def obtener_coordenadas(self, direccion):
        geolocalizador = Nominatim(user_agent="mi_aplicacion")
        ubicacion = geolocalizador.geocode(direccion)
        if ubicacion is not None:
            latitud = ubicacion.latitude
            longitud = ubicacion.longitude
            return f"{latitud},{longitud}"
        else:
            return None, None


    def register(self):
        datos_cliente = []
        datos_cliente.append(self.entryCelular.get())
        datos_cliente.append(self.entryCorreo.get())
        datos_cliente.append(self.medio_pago.get())
        datos_cliente.append(self.entryNombre.get())
        datos_cliente.append(self.entryapellido.get())
        datos_cliente.append(self.entrydocumento.get())
        datos_cliente.append(self.entrydireccion.get())
        coordenadas = self.obtener_coordenadas(self.entrydireccion.get())
        datos_cliente.append(coordenadas)
        datos_cliente.append(self.direccionRecibo)


        if "" in datos_cliente:
            messagebox.showerror(message="Porfavor ingresa todos los datos",title="Mensaje") 

        elif not(self.entrydocumento.get().isdigit()):
            messagebox.showerror(message="Porfavor ingresa un numero de documento valido",title="Mensaje") 

        elif not(self.entryCelular.get().isdigit()):
            messagebox.showerror(message="Porfavor ingresa un numero de celular valido",title="Mensaje") 

        elif coordenadas == (None, None):
            messagebox.showerror(message="Por favor ingresa una direccion Valida",title="Mensaje") 
        
        else:
            try:
                conexionDB.insertar(datos_cliente, "CLIENTE")
                nombre_usuario = conexionDB.consultar(f"SELECT usuario FROM cliente ORDER BY CAST(SUBSTRING(usuario, 3, 4) AS INTEGER) DESC LIMIT 1;")
                messagebox.showinfo(message=f"Ya estas registrado, tu correo y contraseña son {nombre_usuario[0][0]}",title="Mensaje") 
                self.ventana.destroy()

            except psycopg2.errors.UniqueViolation as e:
                messagebox.showinfo(message=f"El numero de celualr ya esta registrado.",title="Mensaje") 
                conexionDB.conexion.rollback()

            except Exception as e:
                messagebox.showinfo(message=f"Tu correo es invalido",title="Mensaje") 
                conexionDB.conexion.rollback()
