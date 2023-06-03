from ConexionDB import Conexion


class Temas:

    _INSERTAR = "INSERT INTO temas(tema) VALUES(%s)"
    _SELECCIONARTODOS = "SELECT * FROM temas"

    @classmethod
    def insertar_tema(cls, tema: str):
        try:
            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._INSERTAR, (tema,))
        except Exception as e:
            print(e)

    @classmethod
    def seleccionar_temas(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONARTODOS)
                temas = [tema[0] for tema in cursor.fetchall()]
                return temas


if __name__ == '__main__':
    db = Temas()
    print(db.seleccionar_temas())
