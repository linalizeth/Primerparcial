import src.config.globals as globals

class modelo1:
    def metodo1(self):
        cursor = globals.DB.cursor()

        cursor.execute('SELECT * FROM products')

        products = cursor.fetchall()

        cursor.close()

        return products