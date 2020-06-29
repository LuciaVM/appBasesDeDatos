from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from enfermedad import Enfermedad
from grupoGenes import GrupoGenes
from grupoVariantes import GrupoVariantes
from ventanasApp.ventanaGenes import VentanaGenes
from ventanasApp.ventanaInfoEnfermedades import VentanaInfoEnfermedad
from ventanasApp.ventanaVariantes import VentanaVariantes


class VentanaAreaGenetica:
    raiz = 0
    def __init__(self, raizAntigua, db):
        # Primero, creamos los elementos de la ventana y los situamos
        raizAntigua.destroy()
        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Genetic window')

        # Boton de salir
        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command= lambda :raiz.destroy())
        self.bSalir.place(x=900, y=550, width=90, height=90)

        self.lIntroduccion = Label(raiz, text='Enter one disease name:', bg="navy", fg="white",
                                   font=("Verdana", 20))
        self.lIntroduccion.place(x=0, y=0, width=1200, height=60)

        self.lNombre = Label(raiz, text='Disease name:', bg="light cyan", fg="black")
        self.lNombre.place(x=30, y=200, width=200, height=30)
        self.tNombre = ttk.Entry(raiz)
        self.tNombre.place(x=260, y=200, width=900, height=30)
        self.bInformacion = ttk.Button(raiz, text = 'Info about the disease', command=lambda: mostrarInfoEnfermedad(raiz, db, self.tNombre.get()))
        self.bInformacion.place(x=180, y=400, width=150, height=50)

        self.bInformacion = ttk.Button(raiz, text='Related genes', command = lambda :mostrarGenes(raiz, db, self.tNombre.get()))
        self.bInformacion.place(x=480, y=400, width=150, height=50)

        self.bInformacion = ttk.Button(raiz, text='Related gene variants', command = lambda : mostrarVariantes(raiz, db, self.tNombre.get()))
        self.bInformacion.place(x=780, y=400, width=150, height=50)

        raiz.mainloop()

def mostrarInfoEnfermedad(raiz, db, nombre):
    enfermedad = Enfermedad(db, nombre)
    v = VentanaInfoEnfermedad(raiz, enfermedad)

def mostrarVariantes(raiz, db, nombre):
    enfermedad = Enfermedad(db, nombre)
    variantes = GrupoVariantes(baseDeDatos=db, enfermedadID= enfermedad.ID)
    n = VentanaVariantes(raiz, variantes)

def mostrarGenes(raiz, db, nombre):
    enfermedad = Enfermedad(db, nombre)
    genes = GrupoGenes(baseDeDatos=db, enfermedadID= enfermedad.ID)
    n = VentanaGenes(raiz, genes)



