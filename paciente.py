
class Paciente:

    def __init__(self, baseDeDatos, nombre, apellidos):
        self.bd = baseDeDatos
        self.nombrePaciente = nombre
        self.apellidosPaciente = apellidos

        ## Creamos la setencia que se traiga los datos del paciente a partir de su nombre y apellidos

        sentencia = """SELECT * FROM paciente p WHERE p.Nombre =\"""" + self.nombrePaciente + """\" && p.Apellidos =\"""" + self.apellidosPaciente + """\";"""

        datos = self.bd.select(sentencia)
        if len(datos)==1:
            self.dni = datos[0].get('DNI')
            self.nombre = datos[0].get('Nombre')
            self.apellidos = datos[0].get('Apellidos')
            self.sexo = datos[0].get('Sexo')
            self.telefono = datos[0].get('Telefono')
            self.fechaNacimiento = datos[0].get('FechaNac')
            self.enfermedadID = datos[0].get('Enfermedad_idEnfermedad')

            sentencia2 = """SELECT NombreEnfermedad FROM bdbnoindices.enfermedad WHERE idEnfermedad = \"""" + self.enfermedadID + """\" ;"""
            nombreEnf = self.bd.select(sentencia2)

            self.enfermedad = nombreEnf[0].get('NombreEnfermedad')

        else:
            print("Ha habido un error")

    def getDNI(self):
        return self.dni

    def getNombre(self):
        return self.nombrePaciente

    def getApellidos(self):
        return self.apellidosPaciente

    def getEnfermedad(self):
        return self.enfermedad

    def getFechaNaciemiento(self):
        return self.fechaNacimiento

    def getSexo(self):
        return self.sexo

    def getTelefono(self):
        return self.telefono

