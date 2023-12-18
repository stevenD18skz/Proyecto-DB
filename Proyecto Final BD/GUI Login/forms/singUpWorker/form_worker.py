from forms.singUpWorker.form_worker_designer import FormRegisterWorkerDesigner
from tkinter import messagebox
import tkinter as tk
import conexionDB
from geopy.geocoders import Nominatim


class FormWorker(FormRegisterWorkerDesigner):
    def __init__(self):
        super().__init__()

    """
    funcion que dada una direccino obtiene la ltidud y lingitud de esta
    """
    def obtener_coordenadas(self, direccion):
        geolocalizador = Nominatim(user_agent="mi_aplicacion")
        ubicacion = geolocalizador.geocode(direccion)
        if ubicacion is not None:
            latitud = ubicacion.latitude
            longitud = ubicacion.longitude
            return f"{latitud},{longitud}"
        else:
            return None, None


    """
    con los datos que el usuario lleno en la ventan
    lo registra en la base de datos en la parte de trabajador
    """
    def register(self):
        datos_trabajador = [self.direccionPerfil , self.direccionDocumento ]
        coordenadas = self.obtener_coordenadas(self.entrydireccion.get())
        datos_trabajador.append(coordenadas)
        datos_trabajador.append(self.entrydireccion.get())
        datos_trabajador.append(self.entryUsuario.get())
        datos_trabajador.append(self.entryapellido.get())
        datos_trabajador.append(self.entrydocumento.get())
        datos_trabajador.append(0.0)

        if "" in datos_trabajador:
            messagebox.showerror(message="Por favor ingresa todos los datos",title="Mensaje") 

        elif not(self.entrydocumento.get().isdigit()):
            messagebox.showerror(message="Por favor ingresa un numero de documento valido",title="Mensaje") 

        elif coordenadas == (None, None):
            messagebox.showerror(message="Por favor ingresa una direccion Valida",title="Mensaje") 
        
        else:
            conexionDB.insertar(datos_trabajador, "TRABAJADOR")
            nombre_usuario = conexionDB.consultar(f"SELECT id_trabajador FROM trabajador ORDER BY CAST(SUBSTRING(id_trabajador, 3, 4) AS INTEGER) DESC LIMIT 1;")
            messagebox.showinfo(message=f"Ya estas registrado, tu usuario y contraseña son {nombre_usuario[0][0]}",title="Mensaje") 
            self.ventana.destroy()


        
        
