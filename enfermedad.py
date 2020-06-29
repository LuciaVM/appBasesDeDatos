class Enfermedad():
    def __init__(self, baseDeDatos, nombre):
        sentencia = """SELECT * FROM """+baseDeDatos.nameDB+""".enfermedad where NombreEnfermedad = \"""" + nombre + """\";"""
        datos = baseDeDatos.select(sentencia)
        if (len(datos)<1):
            print("Encontramos más de dos enfermedades con ese nombre")
            print(datos)
        else:
            self.ID = datos[0].get('idEnfermedad')
            self.nombre = datos[0].get('NombreEnfermedad')
            self.sintomas = datos[0].get('Sintomas')
