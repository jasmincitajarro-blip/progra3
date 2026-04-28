from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['La guitarra', 'Para no verte más', 'Balada para una chica']
    return render_template('lista3.html', titulo='canciones', musicas=lista)