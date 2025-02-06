from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/accueil') 

def index():
    return render_template("index.html")

app.run(debug=True ) 

@app.route('/accueil')
def accueil():
    t = "Accueil" # code Python standard
    n = "Henri"
    return render_template("index.html", titre=t, nom=n)