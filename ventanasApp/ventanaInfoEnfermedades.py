from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class VentanaInfoEnfermedad:
    raiz = 0
    def __init__(self, raizAntigua, enfermedad):
        self.raizAntigua = raizAntigua
        self.enfermedad = enfermedad
        raizAntigua.destroy()
        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Info disease')

        self.lIntroduccion = Label(raiz, text='Information about the disease', bg="navy", fg="white",
                                   font=("Verdana", 20))

        self.lID = Label(raiz, text='ID:', bg="light cyan", fg="black")
        self.lNombre = Label(raiz, text='Name:', bg="light cyan", fg="black")
        self.lSymptoms = Label(raiz, text='Symptoms:', bg="light cyan", fg="black")

        self.tID = ttk.Entry(raiz)
        self.tNombre = ttk.Entry(raiz)
        self.tSymptoms = Text(raiz)

        self.lIntroduccion.place(x=0, y=0, width=1200, height=60)

        self.lID.place(x=75, y= 75, width=75, height=40)
        self.tID.place(x=200, y=75, width=800, height=40)
        self.lNombre.place(x=75, y=150, width=75, height=40)
        self.tNombre.place(x=200, y=150, width=800, height=40)
        self.lSymptoms.place(x=75, y=225, width=75, height=40)
        self.tSymptoms.place(x=200, y=225, width=800, height=300)


        self.tID.insert(0, enfermedad.ID)

        self.tNombre.insert(0, enfermedad.nombre)

        self.tSymptoms.insert("1.0", enfermedad.sintomas)

        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command=lambda: raiz.destroy())
        self.bSalir.place(x=900, y=550, width=90, height=90)

        raiz.mainloop()

