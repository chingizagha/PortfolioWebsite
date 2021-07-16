from portfolio import db

class Profile(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     age = db.Column(db.Integer, nullable=False)
     location = db.Column(db.String(80), nullable=False)
     desc = db.Column(db.Text, nullable=False)
     image = db.Column(db.String(20), nullable=True)

class Project(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     tag = db.Column(db.String(80), nullable=False)
     tech = db.Column(db.String(80), nullable=False)
     desc = db.Column(db.String(50), nullable=False)
     info = db.Column(db.String(80), nullable=False)
     link = db.Column(db.String(80), nullable=False)
     image = db.Column(db.String(20), nullable=True)

class Blog(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     desc = db.Column(db.String(50), nullable=False)
     link = db.Column(db.String(80), nullable=False)
     image = db.Column(db.String(20), nullable=True)

class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)






