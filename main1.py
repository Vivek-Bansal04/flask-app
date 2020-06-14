from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import json
from werkzeug.utils import secure_filename
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)



class Forms(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=True)
    name_animal = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    current_state = db.Column(db.String(80), nullable = False)
    loc_user = db.Column(db.String(120), nullable=False)
    name_user = db.Column(db.String(80), nullable=False)
    ph_num = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=False)



@app.route("/")
def home():
    return render_template('home.html')


@app.route("/post", methods= ['GET', 'POST'])
def upload():
    if (request.method == 'POST'):
        '''Add entry to database'''
        file = request.files['inputFile']
        animal_name = request.form.get('animal_name')
        description = request.form.get('description')
        option = request.form.get('condition')
        location = request.form.get('location')
        user_name = request.form.get('user_name')
        phone = request.form.get('phone')

        entry = Forms(image=file.read(), name_animal=animal_name, description=description, current_state=option, loc_user=location, name_user=user_name, ph_num=phone, date=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template('form.html')



app.run(debug=True)