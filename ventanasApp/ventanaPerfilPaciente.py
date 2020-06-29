from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from historialTratamientos import HistorialTratamientos


class VentanaPerfilPaciente:
    raiz = 0

    def __init__(self, raizAntigua, db, paciente):
        raizAntigua.destroy()
        raiz = Tk()
        raiz.geometry('1200x700')
        raiz.configure(bg="deep sky blue")
        raiz.resizable(width=False, height=False)
        raiz.title('Patients window')

        self.lIntroduccion = Label(raiz, text='Patient profile', bg="navy", fg="white",
                                   font=("Verdana", 20))
        self.lNombre = Label(raiz, text='Name:', bg="light cyan", fg="black")
        self.lApellidos = Label(raiz, text='Surnames:', bg="light cyan", fg="black")
        self.lDNI = Label(raiz, text='DNI:', bg="light cyan", fg="black")
        self.lDisease = Label(raiz, text='Disease:', bg="light cyan", fg="black")
        self.lSexo = Label(raiz, text='Sex:', bg="light cyan", fg="black")
        self.lPhone = Label(raiz, text='Phone:', bg="light cyan", fg="black")
        self.lBirthDate = Label(raiz, text='Date of birth:', bg="light cyan", fg="black")
        self.lHistorialMedicacion = Label(raiz, text='Treatment history:', bg="light cyan", fg="black")


        self.tNombre = ttk.Entry(raiz, width=20)
        self.tApellidos = ttk.Entry(raiz, width=20)
        self.tDNI = ttk.Entry(raiz, width=20)
        self.tDisease = ttk.Entry(raiz, width=20)
        self.tSexo = ttk.Entry(raiz, width=20)
        self.tPhone = ttk.Entry(raiz, width=20)
        self.tBirthDate = ttk.Entry(raiz, width=20)
        self.tHistorial = Text(raiz, width=340, height=60)

        self.tNombre.insert(0, paciente.getNombre())
        self.tApellidos.insert(0, paciente.getApellidos())
        self.tSexo.insert(0, paciente.getSexo())
        self.tDNI.insert(0, paciente.getDNI())
        self.tDisease.insert(0, paciente.getEnfermedad())
        self.tPhone.insert(0, paciente.getTelefono())
        self.tBirthDate.insert(0, paciente.getFechaNaciemiento())


        self.lNombre.place(x=120, y=100, width=100, height=30)
        self.lApellidos.place(x=650, y=100, width=100, height=30)
        self.lDNI.place(x=120, y=150, width=100, height=30)
        self.lDisease.place(x=650, y=150, width=100, height=30)
        self.lSexo.place(x=120, y=200, width=100, height=30)
        self.lBirthDate.place(x=650, y=200, width=100, height=30)
        self.lPhone.place(x=120, y=250, width=100, height=30)
        self.lHistorialMedicacion.place(x=120, y=300, width=100, height=30)

        self.tNombre.place(x=220, y=100, width=320, height=30)
        self.tApellidos.place(x=750, y=100, width=320, height=30)
        self.tDNI.place(x=220, y=150, width=320, height=30)
        self.tDisease.place(x=750, y=150, width=320, height=30)
        self.tSexo.place(x=220, y=200, width=320, height=30)
        self.tBirthDate.place(x=750, y=200, width=320, height=30)
        self.tPhone.place(x=220, y=250, width=320, height=30)
        self.tHistorial.place(x= 240, y = 300, width=500, height=300)

        self.lIntroduccion.place(x=0, y=0, width=1200, height=60)

        # También, vamos a meter el historial de medicacion
        historial = HistorialTratamientos(baseDeDatos=db, dni= paciente.dni)
        textoHistorial = ""
        for i in range(len(historial.listaTratamientos)):

            id = historial.listaTratamientos[i].id
            nombre = historial.listaTratamientos[i].nombre
            prinActivo = historial.listaTratamientos[i].principioActivo
            envase = historial.listaTratamientos[i].envase
            excipiente = historial.listaTratamientos[i].excipiente
            fechIn = historial.listaTratamientos[i].fechaInicio
            fechFin = historial.listaTratamientos[i].fechaFin
            dosis = historial.listaTratamientos[i].dosis

            textoHistorial += "TREATMENT " + str(i + 1) + ": \n"
            textoHistorial += "ID: " + id + " \n"
            textoHistorial += "Name: " + nombre + " \n"
            textoHistorial += "Active ingredient: " + prinActivo + " \n"
            textoHistorial += "Package: " + envase + " \n"
            textoHistorial += "Excipient: " + excipiente + " \n"
            textoHistorial += "Dose: " + dosis + " \n"
            textoHistorial += "Start date: " + fechIn + " \n"
            textoHistorial += "End date: " + fechFin + ". \n"
            textoHistorial += "\n"

        self.tHistorial.insert("1.0", textoHistorial)

        # Boton de salir
        imagenBotonSalir = Image.open("iconos\\botonSalirRedimensionado.png")
        imagenBotonSalir = imagenBotonSalir.resize((80, 80), Image.ANTIALIAS)
        imagenBotonSalir = ImageTk.PhotoImage(imagenBotonSalir)
        self.bSalir = ttk.Button(raiz, image=imagenBotonSalir, command=lambda: raiz.destroy())
        self.bSalir.place(x=900, y=450, width=90, height=90)

        raiz.mainloop()

