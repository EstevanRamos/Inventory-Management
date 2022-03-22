from email.policy import default
from operator import index
from sqlalchemy import PrimaryKeyConstraint, true
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    commoditys = db.relationship('Commodity' , backref = 'factored_by', lazy = True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(60), index = True)
    entry_type = db.Column(db.String(10), index = True)
    quantity = db.Column(db.String(10), index = True)
    datein = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    dateout = db.Column(db.DateTime, index = True)
    shipper = db.Column(db.String(60), index = True)
    consignee = db.Column(db.String(60), index = True)
    customer = db.Column(db.String(60), index = True)
    notes = db.Column(db.Text)
    status = db.Column(db.String(60), index = True)

    def __repr__(self):
        return '<Commodity {}>'.format(self.item)

    def to_dict(self):
        return {
            'item': self.item,
            'entry_type': self.entry_type,
            'quantity': self.quantity,
            'datein': self.datein,
            'dateout': self.dateout,
            'shipper': self.shipper,
            'consignee': self.consignee,
            'customer': self.customer,
            'notes': self.notes,
            'status':self.status
        }


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    whatsapp = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)