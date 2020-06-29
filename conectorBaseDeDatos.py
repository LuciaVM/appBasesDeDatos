import pymysql as pymysql


class BaseDeDatos:
    def __init__(self, host, user, password, db, charset, nameDB):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.nameDB = nameDB

    def crearConexion(self):
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def cerrarConexion(self, conexion):
        conexion.close()

    def select(self, sentencia):
        conexion = self.crearConexion()
        lista = list()
        try:
            with conexion.cursor() as cursor:
                sql = sentencia
                cursor.execute(sql)
            for row in cursor:
                lista.append(row)
            return lista
        finally:
            self.cerrarConexion(conexion)

    def getNameDB(self):
        return self.nameDB