from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class VentanaGenes():
    raiz = 0

    def __init__(self, raizAntigua, genes):
        # Primero, creamos los elementos de la ventana y los situamos
        raizAntigua.destroy()
        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Variant window')

        self.lIntroduccion = Label(raiz, text='Genes of entered disease', bg="navy", fg="white",
                                   font=("Verdana", 20))
        self.lIntroduccion.place(x=0, y=0, width=1200, height=60)

        self.tGenes = Text(raiz)
        self.scroll = ttk.Scrollbar(self.tGenes)
        self.tGenes.place(x=200, y=120, width=800, height=380)

        self.tGenes.insert("1.0", genes.toString)

        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command=lambda: raiz.destroy())
        self.bSalir.place(x=900, y=550, width=90, height=90)

        raiz.mainloop()

