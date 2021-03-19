import src.config.globals as globals
from src.config.db import createDB
from flask import render_template,redirect, url_for, request
from src import app
from os import path
from src.models.basedato import DB


CONEXION_PATH = path.abspath('src/config/conexion.json')

@app.route('/')
def index():
    if path.exists(CONEXION_PATH):
        createDB()
    elif globals.DB == False:
        return render_template('configuracion.html')
    

    basedato = DB()

    return render_template('home.html', basedatos= basedato.basedato())

@app.route('/tabla/<nombre>')
def verTablas(nombre):
    basedato = DB()

    tabla = basedato.exportarTabla(nombre)

    return render_template('tabla.html', tabla=tabla)

@app.route('/descripcion/<nombre>')
def descripTabla(nombre):
    basedato = DB()

    descripcion = basedato.descripTabla(nombre)

    return render_template('descripcion.html', Descripcion=descripcion)