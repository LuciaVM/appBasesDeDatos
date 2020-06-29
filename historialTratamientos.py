from tratamiento import TratamientoPaciente


class HistorialTratamientos:
    def __init__(self, baseDeDatos, dni):
        sentencia = """SELECT * FROM """ + baseDeDatos.getNameDB() + """.tiene where Paciente_DNI = \"""" + dni + """\" order by Fecha_inicio;"""

        datos = baseDeDatos.select(sentencia)
        self.listaTratamientos = list()
        for i in range(len(datos)):
            # Creamos una instancia de medicamento y la guardamos en la lista. El tratamiento tendra:
            # ID(2), Fecha_inicio(3), Fecha_final (4), Dosis(5)
            # Nombre (2), principioActivo(3), excipiente(4), envase(5)
            ID = datos[i].get('Tratamiento_idTratamiento')
            fechaInicio = datos[i].get('Fecha_inicio')
            fechaFin = datos[i].get('Fecha_final')
            dosis = datos[i].get('Dosis')

            sentenciaTratamiento = """SELECT * FROM """ + baseDeDatos.getNameDB() + """.tratamiento where idTratamiento = """ + str(ID) + """;""";
            datosTratamientoI = baseDeDatos.select(sentenciaTratamiento)
            nombre = datosTratamientoI[0].get('NombreTratamiento')
            principioActivo = datosTratamientoI[0].get('PrincipioActivo')
            excipiente = datosTratamientoI[0].get('Excipiente')
            envase = datosTratamientoI[0].get('Envase')

            tratamiento = TratamientoPaciente(id=ID, fechaInic = fechaInicio, fechaFin= fechaFin, dosis=dosis, nombre=nombre, principioAct = principioActivo, excipiente= excipiente, envase = envase)
            self.listaTratamientos.append(tratamiento)


