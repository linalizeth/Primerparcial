from flask import redirect, request, url_for
from src.config.db import createDB, installDB
from src import app
import json

@app.route('/configuracion', methods=['POST'])
def configuracion():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    servidor = request.form.get('servidor')
    puerto = request.form.get('puerto')

    dbData = {
        'host' : servidor,
        'port' : int(puerto),
        'user' : usuario,
        'password' : password,
      
    }

    file = open('src/config/conexion.json', 'w')
    file.write(json.dumps(dbData))
    file.close()

    createDB()
    installDB()

    return redirect(url_for('index'))