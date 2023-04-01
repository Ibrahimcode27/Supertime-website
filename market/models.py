from market import db

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=25),nullable=False,unique=True)
    email_address = db.Column(db.String(length=50),nullable=False)
    password = db.Column(db.String(length=30),nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    Type = db.Column(db.String(length=30),nullable=False)
    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False,unique=True)
    description = db.Column(db.String(length=1024),nullable=False,unique=True)

    def __repr__(self):
        return f'Item {self.Type}'