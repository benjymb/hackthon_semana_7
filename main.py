# Cree un sistema para hacer el registro de notas de alumnos
from modelos import Docente, Alumno
from app import Aplicacion
from conexion import conexion_mdb, conexion_pg
import atributos_conexion


def _inicializar_cx():
    cx_mongodb = conexion_mdb.ConexionMDB(
        atributos_conexion.CADENA_DE_CONEXION_MONGODB,
        atributos_conexion.BASE_DATOS_MONGODB,
        atributos_conexion.COLECCION_MONGODB
    )
    cx_postgres = conexion_pg.ConexionPG(
        direccion_servidor=atributos_conexion.DIRECCION_SERVIDOR_POSTGRES,
        usuario=atributos_conexion.USUARIO_POSTGRES,
        contrasena=atributos_conexion.CONTRASENIA_POSTGRES,
        base_datos=atributos_conexion.BASE_DATOS_POSTGRES,
        tabla=""
    )
    return cx_mongodb, cx_postgres


def main():
    app_registro = Aplicacion(*_inicializar_cx())
    print('Bienvenido al sistema de registro de notas de alumnos')
    print('Ingrese 1 para agregar un nuevo docente')
    print('Ingrese 2 para agregar un nuevo alumno')
    print('Ingrese 3 para agregar notas a un alumno')
    opcion = input('Ingrese la opcion : ')
    if opcion == '1':
        docente_1 = app_registro.registrar_docente()
        print(docente_1)
    elif opcion == '2':
        alumno_1 = app_registro.registrar_alumno()
        print(alumno_1)
    elif opcion == '3':
        alumno_1 = app_registro.buscar_alumno()
        alumno_1 = app_registro.registrar_nota_alumno(alumno_1)
        print(alumno_1)

main()
