from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging


logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:root@localhost:5432/fog'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate()

class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150) ,unique =True)
    city = db.Column(db.String(150))
    address = db.Column(db.String(150))
    pin = db.Column(db.Integer)

    def __init__(self,name,city,address,pin):
        self.name =name
        self.city = city
        self.address = address
        self.pin = pin

@app.route("/data/", methods=['POST', 'GET'])
def data():

    # Inserting the data into the table
    if request.method == 'POST':
        db_data = request.get_json()

        name = db_data['name']
        city = db_data['city']
        address =db_data['address']
        pin = db_data['pin']

        college = students(name,city,address,pin)

        db.session.add(college)
        db.session.commit()
        return jsonify({'Status':'Record added succesfully'}),201


    # Get all the data from database
    if request.method == 'GET':
        college =[]
        all_students = students.query.all()
        for student in all_students:
            results = {
                    "id":student.id,
                    "name":student.name,
                    "city":student.city,
                    "address":student.address,
                    "pin":student.pin, }
            college.append(results)
        return jsonify(
            {
                "success":True,
                "all_students": college
            })


@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    #GET a specific data by id
    if request.method == 'GET':
        college = students.query.get(id)
        print(college)

        dataDict = {
            'name': str(college.name),
            'city': str(college.city),
            'address': str(college.address),
            'pin': str(college.pin)
        }
        return jsonify({'students':dataDict}),200

    # DELETE the in the table
    if request.method =='DELETE':
        delData = students.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status':'one id'+id+' is deleted'}),200

    # Update the data in table
    if request.method == 'PUT':
         get_req = request.get_json()
         newName = get_req['name']
         newCity = get_req['city']
         newAddress = get_req['address']
         newPin = get_req['pin']

         editData = students.query.filter_by(id=id).first()

         editData.name = newName
         editData.city = newCity
         editData.address = newAddress
         editData.pin =  newPin
         db.session.commit()
         return jsonify({'status':'Data is Updated successfully'}),201


if __name__ == '__main__':
    app.run(debug=True)
