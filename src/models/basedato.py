import src.config.globals as globals

class DB:
    def basedato(self):
        cursor = globals.DB.cursor()

        cursor.execute('SHOW DATABASES')

        basedato = cursor.fetchall()

        cursor.close()

        return basedato

    def exportarTabla(self, nombre):
        print(globals.DB)
        cursor = globals.DB.cursor()
        query = "use " + nombre

        cursor.execute(query)
        cursor.execute('SHOW TABLES')

        tabla = cursor.fetchall()

        cursor.close()

        return tabla

    def descripTabla(self, nombre):
        cursor = globals.DB.cursor()
        query = "desc " + nombre

        cursor.execute(query)

        desctable = cursor.fetchall()

        cursor.close()

        print(desctable)

        return desctable