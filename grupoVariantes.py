
class GrupoVariantes:
    def __init__(self, baseDeDatos, enfermedadID):
        sentencia = """SELECT * FROM """ + baseDeDatos.nameDB + """.causadapor where Enfermedad_idEnfermedad = \"""" + enfermedadID + """\";"""
        datosRelacion = baseDeDatos.select(sentencia)
        self.listaTratamientos = list()
        resultado = ""
        for i in range(len(datosRelacion)):
            idVariante = datosRelacion[i].get('Variante_idVariante')
            ei = datosRelacion[i].get('Evidence_index')
            np = datosRelacion[i].get('Num_publicaciones')
            sentencia2 = """SELECT * FROM """ + baseDeDatos.nameDB + """.variante where idVariante = \"""" + idVariante + """\";"""
            datosVariante = baseDeDatos.select(sentencia2)
            posicion = datosVariante[0].get('PosicionVariante')
            gen = datosVariante[0].get('Gen_idGen')
            numero = str(i+1)
            resultado += "VARIANT " + numero + ": \n"
            resultado += "ID: " + idVariante + "\n"
            resultado += "In gen: " + str(gen) + "\n"
            resultado += "In position: " + str(posicion) + "\n"
            resultado += "Evidence index: " + str(ei) + "\n"
            resultado += "Number of apparitions in publications: " + str(np) + "\n"
            resultado += "\n"

        self.toString = resultado