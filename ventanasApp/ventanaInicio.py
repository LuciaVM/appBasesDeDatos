

from conectorBaseDeDatos import BaseDeDatos
from ventanasApp.ventanaAreaGenetica import VentanaAreaGenetica

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from ventanasApp.ventanaAreaPacientes import VentanaAreaPacientes


class VentanaInicio:
    raiz = 0

    def __init__(self, db):

        # Primero, creamos los elementos de la ventana y los situamos
        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Start window')

        self.lIntroduccion = Label(raiz, text='WELCOME! Choose one area:', bg="navy", fg="white",
                                   font=("Verdana", 20))
        self.lIntroduccion.place(x=0, y=0, width=1200, height=60)

        iconoPaciente = Image.open("iconos\\iconoPacientes.png")
        iconoPaciente = iconoPaciente.resize((200, 200), Image.ANTIALIAS)
        iconoPaciente = ImageTk.PhotoImage(iconoPaciente)


        self.botonPacientes = ttk.Button(raiz, image=iconoPaciente, command=lambda : seleccionaAreaPacientes(raiz, db))

        self.botonPacientes.place(x=280, y=200, width=200, height=200)

        iconoGenetica = Image.open("iconos\\iconoGenetica.jpg")
        iconoGenetica = iconoGenetica.resize((200, 200), Image.ANTIALIAS)
        iconoGenetica = ImageTk.PhotoImage(iconoGenetica)


        self.botonGenetica = ttk.Button(raiz, image=iconoGenetica,
                                        command=lambda: seleccionaAreaGenetica(raiz, db))
        self.botonGenetica.place(x=650, y=200, width=200, height=200)

        self.lAreaPacientes = Label(raiz, text='Patient area', bg="light cyan", fg="black",
                                    font=("Verdana", 18))
        self.lAreaPacientes.place(x=280, y=420, width=200, height=30)

        self.lAreaGenetica = Label(raiz, text='Genetic area', bg="light cyan", fg="black",
                                   font=("Verdana", 18))
        self.lAreaGenetica.place(x=650, y=420, width=200, height=30)

        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command=raiz.destroy)
        self.bCargarInformacion = ttk.Button(raiz, text="Show patient profile", command=raiz.destroy)
        self.bSalir.place(x=900, y=550, width=90, height=90)

        raiz.mainloop()


def seleccionaAreaGenetica(raiz, db):
    nueva = VentanaAreaGenetica(raiz, db)

def seleccionaAreaPacientes(raiz, db):
    nueva = VentanaAreaPacientes(raiz, db)

def main():
    prueba = BaseDeDatos(host='localhost', user='root', password='sscdrsnshsm', db='bdbnoindices', charset='utf8',nameDB='bdbnoindices')
    db= BaseDeDatos(host='localhost', user='root', password='sscdrsnshsm', db='bdbnoindices', charset='utf8', nameDB = 'bdbnoindices')
    mi_app = VentanaInicio(prueba)
    return 0

if __name__ == '__main__':
    main()
