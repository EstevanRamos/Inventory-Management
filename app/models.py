from email.policy import default
from operator import index
from sqlalchemy import PrimaryKeyConstraint, true
from sqlalchemy.orm import relationship
from app import db
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'customer' 
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    whatsapp = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.first_name)

class Commodity(db.Model):
    __tablename__ = 'commodity'
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(60), index = True)
    entry_type = db.Column(db.String(10), index = True)
    quantity = db.Column(db.String(10), index = True)
    datein = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    dateout = db.Column(db.DateTime, index = True)
    notes = db.Column(db.Text)
    status = db.Column(db.String(60), index = True)

    shipper_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    consignee_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    shipper = relationship('Customer', foreign_keys = [shipper_id])
    consignee = relationship('Customer', foreign_keys = [consignee_id])
    c = relationship('Customer', foreign_keys = [customer_id])

   
    def __repr__(self):
        return '<Commodity {}>'.format(self.item)

    def to_dict(self):
        return {
            'item': self.item,
            'entry_type': self.entry_type,
            'quantity': self.quantity,
            'datein': self.datein,
            'dateout': self.dateout,
            'shipper': self.shipper.first_name +" " +self.shipper.last_name,
            'consignee': self.consignee.first_name +" " +self.consignee.last_name,
            'customer': self.c.first_name + " " +self.c.last_name,
            'notes': self.notes,
            'status':self.status
        }


