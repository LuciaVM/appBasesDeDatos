class GrupoGenes:
    def __init__(self, baseDeDatos, enfermedadID):
        sentencia = """SELECT * FROM """ + baseDeDatos.nameDB + """.relacionadacon where Enfermedad_idEnfermedad = \"""" + enfermedadID + """\";"""
        datosRelacion = baseDeDatos.select(sentencia)
        self.listaGenes = list()
        resultado = ""
        for i in range(len(datosRelacion)):
            idGen = datosRelacion[i].get('Gen_idGen')
            sentencia2 = """SELECT * FROM """ + baseDeDatos.nameDB + """.gen where idGen = """ + str(idGen) + """;"""
            datosGen = baseDeDatos.select(sentencia2)
            simbolo = datosGen[0].get('Simbolo')
            cromosoma = datosGen[0].get('Cromosoma')
            numero = str(i+1)
            resultado += "Gen " + numero + ": \n"
            resultado += "ID: " + str(idGen) + "\n"
            resultado += "Symbol: " + simbolo + "\n"
            resultado += "In chromosome: " + str(cromosoma) + "\n"
            resultado += "\n"

        self.toString = resultado