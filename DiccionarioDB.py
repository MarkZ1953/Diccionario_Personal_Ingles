from Conexion import Conexion


class DiccionarioDB:
    _SELECCIONAR = "SELECT * FROM diccionario ORDER BY id_palabra"
    _INSERTAR = 'INSERT INTO diccionario(p_ingles, p_espanol, nota) VALUES(%s, %s, %s)'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)

    @classmethod
    def insertar(cls):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = ("Hello", "Hola", "Saludar a otra persona")
                cursor.execute(cls._INSERTAR, valores)


if __name__ == '__main__':
    DiccionarioDB().insertar()
