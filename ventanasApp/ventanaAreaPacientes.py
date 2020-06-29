from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from paciente import Paciente
from ventanasApp.ventanaPerfilPaciente import VentanaPerfilPaciente


class VentanaAreaPacientes:
    raiz = 0

    def __init__(self, raizAntigua, db):
        # Primero, creamos los elementos de la ventana y los situamos
        raizAntigua.destroy()

        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Patients window')

        self.tNombre = ttk.Entry(raiz, width=20)
        self.tApellidos = ttk.Entry(raiz, width=20)
        self.lIntroduccion = Label(raiz, text='Enter the patient data', bg="navy", fg="white",
                                   font=("Verdana", 20))
        self.lNombre = Label(raiz, text='Name:', bg="light cyan", fg="black")
        self.lApellidos = Label(raiz, text='Surnames:', bg="light cyan", fg="black")

        self.lIntroduccion.place(x=0, y=0, width=1200, height=50)
        self.lNombre.place(x=30, y=120, width=200, height=30)
        self.lApellidos.place(x=30, y=200, width=200, height=30)
        self.tNombre.place(x=260, y=120, width=900, height=30)
        self.tApellidos.place(x=260, y=200, width=900, height=30)

        # Boton de salir
        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command=lambda: raiz.destroy())
        self.bSalir.place(x=900, y=450, width=90, height=90)

        # Boton cargar el perfil del paciente
        self.bCargarInformacion = ttk.Button(raiz, text="Show patient profile",
                                             command=lambda: cargarPerfilDeUnPaciente(db, raiz, self.tNombre.get(),
                                                                                      self.tApellidos.get()))

        self.bCargarInformacion.place(x=400, y=475, width=200, height=50)

        raiz.mainloop()


def cargarPerfilDeUnPaciente(db, raiz, nombre, apellidos):
    paciente = Paciente(db, nombre, apellidos)

    nueva = VentanaPerfilPaciente(raiz, db, paciente)
