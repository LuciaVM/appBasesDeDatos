
from conectorBaseDeDatos import BaseDeDatos
from ventanasApp.ventanaInicio import VentanaInicio


def main():
    prueba = BaseDeDatos(host='localhost', user='root', password='sscdrsnshsm', db='bdbnoindices', charset='utf8',nameDB='bdbnoindices')
    db= BaseDeDatos(host='localhost', user='root', password='sscdrsnshsm', db='bdbnoindices', charset='utf8', nameDB = 'bdbnoindices')
    mi_app = VentanaInicio(prueba)

if __name__ == '__main__':
    main()
