from ConexionDB import Conexion


class FrasesDB:

    _SELECCIONARTODOS = "SELECT * FROM frases"
    _SELECCIONARCATEGORIAS = "SELECT categoria_f FROM frases"
    _SELECCIONARFRASESING = "SELECT f_ingles FROM frases"
    _SELECCIONARFRASESESP = "SELECT f_espanol FROM frases"
    _INSERTAR = "INSERT INTO frases (f_ingles, f_espanol, categoria_f, descripcion_f) VALUES(%s,%s,%s,%s)"

    @classmethod
    def seleccionar_todas_las_frases(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARTODOS)
                return cursor.fetchall()

    @classmethod
    def seleccionar_categorias_frases(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARCATEGORIAS)
                categorias = []
                for categoria in cursor.fetchall():
                    categorias.append(categoria[0])
                return categorias

    @classmethod
    def seleccionar_todas_las_frases_ingles(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARFRASESING)
                frases = []
                for frase in cursor.fetchall():
                    frases.append(frase[0])
                return frases

    @classmethod
    def seleccionar_todas_las_frases_espanol(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARFRASESESP)
                frases = []
                for frase in cursor.fetchall():
                    frases.append(frase[0])
                return frases

    @classmethod
    def insertar_frase(cls, frase_ingles, frase_espanol, categoria, descripcion_frase):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._INSERTAR, (frase_ingles, frase_espanol, categoria, descripcion_frase))

    @classmethod
    def actualizar_frase(cls):
        pass

    @classmethod
    def eliminar_frase(cls):
        pass


if __name__ == '__main__':
    db = FrasesDB()
    print(db.seleccionar_todas_las_frases_ingles())
