from flask import Flask, render_template, request

app = Flask(__name__) # crée une application Web

@app.route('/accueil') # URL http://localhost:5000/index.html

def index():
    return render_template("index.html")

# lien vers le fichier du dossier templates pour générer la page avec Jinja
app.run(debug=True ) # démarre le serveur