import os

from cs50 import SQL
from flask import Flask, render_template, flash, jsonify, redirect, render_template, request, session


app = Flask(__name__)

# Ensure templates are auto-reload
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///schedule.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/x", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Acess form data
        name = request.form.get("name")
        data = request.form.get("data")

        # TODO: Add the user's entry into the database
        db.execute("INSERT INTO schedule (name, data) VALUES(?, ?)", name, data)

        # Go to back to homepage
        return redirect("/x")

    else:

        schedule = db.execute("SELECT * FROM schedule")

        # TODO: Display the entries in the database on index.html

        return render_template("index.html", schedule=schedule)




@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/contatos')
def hello():
    return render_template("contatos.html")

@app.route('/link')
def link():
    return render_template("link.html")

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


# coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)