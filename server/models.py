from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)
    
    animals = db.relationship('Animal', backref='zookeeper')
    def __repr__(self):
        return f'<Pet Owner {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure')
    def __repr__(self):
        return f'<Enclosure is {"open" if self.open_to_visitors else "closed"}>'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    enclosure_by_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    zookeeper_by_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    def __repr__(self):
        return f'<Animal {self.name}>'