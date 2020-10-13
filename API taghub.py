from flask import Flask, render_template, request, redirect, url_for, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask_sqlalchemy import SQLAlchemy

# Oppgave:  Restful API i python
# API som oppretter brukere i PostgreSQL database
# bruker opprettes med: id, brukernavn, epost og passord (id kan opprettes automatisk i databasen) --> hvor brukernavn og epost er  
# unik: sjekk dette --> returner feilmelding hvis de ikker unike

app = Flask(__name__)


def get_all_users():
    return

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        # opprett bruker
        sql = "SELECT "
        return 
    # list opp alle brukerene
    return 


@app.route("/users/<id>", methods=["GET", "DELETE"])
def get_user(id):
    if request.method == "GET":
        # returnere spesifikk bruker: hvis den ikke eksisterer, returner passende status kode
        return
    # slett brukeren: hvis den ikke eksisterer, returner passende status kode
    return


if __name__ == '__main__':
    app.run()
