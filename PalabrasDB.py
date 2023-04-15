from Conexion import Conexion


class PalabrasDB:

    _SELECCIONARTODOS = "SELECT * FROM palabras"
    _SELECCIONARUNO= "SELECT * FROM palabras WHERE id_palabra = %s"
    _INSERTAR = "INSERT INTO palabras(p_ingles, p_espanol, descripcion_p) VALUES(%s, %s, %s)"
    _ELIMINAR = "DELETE FROM palabras WHERE id_palabra = %s"

    @classmethod
    def seleccionar_todas_las_palabras(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARTODOS)
                return cursor.fetchall()

    @classmethod
    def seleccionar_palabra(cls, id_palabra: int):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONARUNO, (id_palabra,))
            return cursor.fetchone()

    @classmethod
    def insertar_palabra(cls, palabra_ingles, palabra_espanol, descripcion):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._INSERTAR, (palabra_ingles, palabra_espanol, descripcion))

    @classmethod
    def eliminar_palabra(cls, id_palabra: int):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (id_palabra,))
