from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:root@localhost:5432/practice'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='rewards')

class UserSchema(ma.Schema):
    class Meta:
        fields = ['id','name']

class RewardSchema(ma.Schema):
    class Meta:
        fields = ['id','reward_name','user_id','user']

@app.route('/')
def index():
    users = User.query.all()
    user_schema = UserSchema(many=True).dump(users)
    # output = user_schema.dump(users).data
    return jsonify({'user' : user_schema})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
