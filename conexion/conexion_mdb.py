from pymongo import MongoClient, errors
from logger import escribir_al_log


class ConexionMDB:

    def __init__(self, cadena_conexion, base_datos, coleccion):
        try:
            self.client = MongoClient(
                cadena_conexion
            )
            self.db = self.client[base_datos]
            self.coleccion = self.db[coleccion]
        except errors.ConnectionFailure as e:
            escribir_al_log(
                e,
                f"Ocurrio un error al conectarnos a la BD MongoDB {base_datos}"
            )

    def __del__(self):
        self.client.close() 

    def insertar_documento(self, datos_documento):
        nuevo_id = None
        try:
            resultado = self.coleccion.insert_one(datos_documento)
            nuevo_id = resultado.inserted_id
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al insertar el documento a la BD MongoDB"
            )
        return nuevo_id

    def obtener_documentos(self, condicion):
        documentos = []
        try:
            respuesta = self.coleccion.find(condicion)
            documentos = list(respuesta)
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al buscar los documentos en la BD MongoDB"
            )
        return documentos

    def obtener_documento(self, condicion):
        documento = None
        try:
            documento = self.coleccion.find_one(condicion)
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al obtener el documento de la BD MongoDB"
            )
        return documento

    def actualizar_documento(self, condicion, atributos_cambiar):
        actualizacion_exitosa = False
        try:
            resultado = self.coleccion.update_one(
                condicion, {
                    '$set': atributos_cambiar
                }
            )
            actualizacion_exitosa = resultado.modified_count > 0
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al actualizar el documento en la BD MongoDB" 
            )
        return actualizacion_exitosa

    def eliminar_documento(self, condicion):
        eliminacion_exitosa = False
        try:
            resultado = self.coleccion.delete_one(
                condicion
            )
            eliminacion_exitosa = resultado.deleted_count > 0
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al eliminar el documento de la BD MongoDB"
            )
        return eliminacion_exitosa
