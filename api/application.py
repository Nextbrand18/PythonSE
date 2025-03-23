#https://www.youtube.com/watch?v=qbLc5a9jdXo&t=1311s

#Setup flask
from flask import Flask 
app = Flask(__name__) 


from flask_sqlalchemy import SQLAlchemy


#configure the db and integrate the db as variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


#store in the db as model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) #no null
    description = db.Column(db.String(120))

#grab the object attributes
    def __repr__(self):
        return f"{self.name} - {self.description}"
        #return f"Drink(name={self.name}, description={self.description})"

#Define a simple route and define a method to hit
@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output =[]
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)

    return {"drinks" : output}
 