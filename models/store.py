import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__='geometry_columns'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    score = db.Column(db.Float)


    def __init__(self, name, score):
        self.name = name
        self.score = score


    def json(self):
        return{'name':self.name ,'score':self.score}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1


  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    #@classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



