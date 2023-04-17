from Conexion import Conexion


class PalabrasDB:

    _SELECCIONARTODOS = "SELECT * FROM palabras"
    _SELECCIONARUNO= "SELECT * FROM palabras WHERE id_palabra = %s"
    _INSERTAR = "INSERT INTO palabras(p_ingles, p_espanol, descripcion_p) VALUES(%s, %s, %s)"
    _ELIMINAR = "DELETE FROM palabras WHERE id_palabra = %s"
    _SELECCIONARPESPANOL = "SELECT * FROM palabras WHERE p_espanol = %s"
    _SELECCIONARPINGLES = "SELECT * FROM palabras WHERE p_ingles = %s"
    _ACTUALIZAR = "UPDATE palabras SET p_espanol=%s,p_ingles=%s,descripcion_p = %s WHERE id_palabra=%s"

    @classmethod
    def seleccionar_todas_las_palabras(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARTODOS)
                return cursor.fetchall()

    @classmethod
    def seleccionar_registro_id(cls, id_palabra: int):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARUNO, (id_palabra,))
                return cursor.fetchone()

    @classmethod
    def seleccionar_registro_p_ingles(cls, palabra_ingles: str):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARPINGLES, (palabra_ingles,))
                return cursor.fetchone()

    @classmethod
    def seleccionar_registro_p_espanol(cls, palabra_espanol: str):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARPESPANOL, (palabra_espanol,))
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

    @classmethod
    def seleccionar_una_columna(cls, columna):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(f"SELECT {columna} FROM palabras")
                palabras = []
                for palabra in cursor.fetchall():
                    palabras.append(palabra[0])
                return palabras

    @classmethod
    def actualizar_registro(cls, palabra_espanol, palabra_ingles, descripcion_palabra, id_palabra):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ACTUALIZAR, (palabra_espanol, palabra_ingles, descripcion_palabra, id_palabra))


if __name__ == '__main__':
    db = PalabrasDB()
    print(db.seleccionar_registro_p_ingles("Hello"))
    print(db.seleccionar_registro_p_espanol("Hola"))
