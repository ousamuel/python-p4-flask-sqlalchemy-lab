#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    
    animal = Animal.query.filter(Animal.id == id).first()
    zookeeper = Zookeeper.query.filter(Zookeeper.id == animal.zookeeper_by_id).first()
    enclosure = Enclosure.query.filter(Enclosure.id == animal.enclosure_by_id).first()
    return f'''
        <ul>Name {animal.name}</ul>
        <ul>Species {animal.species}</ul>
        <ul>Zookeeper {zookeeper.name}</ul>
        <ul>Enclosure {enclosure.environment}</ul>
        
'''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    # return f'''
    response = f'<ul>Name {zookeeper.name}</ul>'
    response += f'<ul>Birthday {zookeeper.birthday}</ul>'
    animals = [animal for animal in zookeeper.animals]
    if animals:
        for animal in animals:
            response += f'<ul>Animal: {animal.name}</ul>'
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    animals = [animal for animal in enclosure.animals]
    response = f'<ul>Environment {enclosure.environment}</ul>'
    response += f'<ul>Open to Visitors {enclosure.open_to_visitors}</ul>'
    if animals:
        for animal in animals:
            response += f'<ul>Animal: {animal.name}</ul>'
    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)
