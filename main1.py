from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import base64
import json
from werkzeug.utils import secure_filename
from datetime import datetime
import pymysql


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
    image = db.Column(db.LargeBinary, nullable=False)
    name_animal = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    current_state = db.Column(db.String(80), nullable=False)
    loc_user = db.Column(db.String(120), nullable=False)
    name_user = db.Column(db.String(80), nullable=False)
    ph_num = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=False)



@app.route("/")
def home():

    data2 = []
    data1 = []
    data2 = Forms.query.order_by(Forms.sno.desc()).all()


    data1 = base64.b64encode(data2[0].image)
    data4 = data1.decode("UTF-8")
    count1 = data2[0].name_animal
    count2 = data2[0].description
    count3 = data2[0].name_user
    count4 = data2[0].loc_user
    count5 = data2[0].current_state

    data6 = base64.b64encode(data2[1].image)
    data7 = data6.decode("UTF-8")
    count6 = data2[1].name_animal
    count7 = data2[1].description
    count8 = data2[1].name_user
    count9 = data2[1].loc_user
    count10 = data2[1].current_state

    data8 = base64.b64encode(data2[2].image)
    data9 = data8.decode("UTF-8")
    count11 = data2[2].name_animal
    count12 = data2[2].description
    count13 = data2[2].name_user
    count14 = data2[2].loc_user
    count15 = data2[2].current_state

    data10 = base64.b64encode(data2[3].image)
    data11 = data10.decode("UTF-8")
    count16 = data2[3].name_animal
    count17 = data2[3].description
    count18 = data2[3].name_user
    count19 = data2[3].loc_user
    count20 = data2[3].current_state

    data12 = base64.b64encode(data2[4].image)
    data13 = data12.decode("UTF-8")
    count21 = data2[4].name_animal
    count22 = data2[4].description
    count23 = data2[4].name_user
    count24 = data2[4].loc_user
    count25 = data2[4].current_state

    return render_template('home.html', data2=data4, num1=data7, num2=data9, num3=data11, num4=data13,
                           counter1=count1, counter2=count2, counter3=count3, counter4=count4, counter5=count5,
                           counter6=count6, counter7=count7, counter8=count8, counter9=count9, counter10=count10,
                           counter11=count11, counter12=count12, counter13=count13, counter14=count14,
                           counter15=count15,
                           counter16=count16, counter17=count17, counter18=count18, counter19=count19,
                           counter20=count20,
                           counter21=count21, counter22=count22, counter23=count23, counter24=count24,
                           counter25=count25)

@app.route("/about")
def about():
    return render_template('about us.html')


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