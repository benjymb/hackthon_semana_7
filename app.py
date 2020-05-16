class Aplicacion:

    def __init__(self, cx_mongodb, cx_postgres):
        self.cx_mongodb = cx_mongodb
        self.cx_postgres = cx_postgres
        self._inicializar_tablas_pg()

    def _inicializar_tabla_profesor(self):
        existe = self.cx_mongodb.obtener_documento(
            {
                'tipo': "CREACION_DB",
                'recurso': 'profesor'
            }
        )
        if not existe:
            self.cx_postgres.crear_tabla(
                """
                CREATE TABLE profesor(
                    id SERIAL,
                    nombre VARCHAR(50) NOT NULL,
                    codigo_docente CHAR(10) NOT NULL
                )
                """
            )
            self.cx_mongodb.insertar_documento(
                {
                    "tipo": "CREACION_DB",
                    "recurso": "profesor"
                }
            )

    def _inicializar_tabla_alumno(self):
        existe = self.cx_mongodb.obtener_documento(
            {
                'tipo': "CREACION_DB",
                'recurso': 'alumno'
            }
        )
        if not existe:
            self.cx_postgres.crear_tabla(
                """
                CREATE TABLE alumno(
                    id SERIAL,
                    nombre VARCHAR(50) NOT NULL,
                    codigo_alumno CHAR(10) NOT NULL
                )
                """
            )
            self.cx_mongodb.insertar_documento(
                {
                    "tipo": "CREACION_DB",
                    "recurso": "alumno"
                }
            )

    def _inicializar_tabla_alumno_notas(self):
        existe = self.cx_mongodb.obtener_documento(
            {
                'tipo': "CREACION_DB",
                'recurso': 'alumno_notas'
            }
        )
        if not existe:
            self.cx_postgres.crear_tabla(
                """
                CREATE TABLE notas_alumno(
                    id SERIAL,
                    id_alumno INTEGER NOT NULL,
                    nota INTEGER NOT NULL
                )
                """
            )
            self.cx_mongodb.insertar_documento(
                {
                    "tipo": "CREACION_DB",
                    "recurso": "notas_alumno"
                }
            )

    def _inicializar_tablas_pg(self):
        self._inicializar_tabla_alumno()
        self._inicializar_tabla_alumno_notas()
        self._inicializar_tabla_profesor()
        
    def registrar_alumno(self):
        pass

    def registrar_docente(self):
        pass

    def registrar_nota_alumno(self):
        pass

    def listar_promedios(self):
        pass