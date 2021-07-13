from portfolio import db

class Profile(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     age = db.Column(db.Integer, nullable=False)
     location = db.Column(db.String(80), nullable=False)
     desc = db.Column(db.Text, nullable=False)
     image = db.Column(db.String(20), nullable=True)

class Education(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(40), nullable=False)
     date = db.Column(db.String(30), nullable=False)
     title = db.Column(db.String(80), nullable=False)
     desc = db.Column(db.Text, nullable=False)
     place = db.Column(db.String(40), nullable=False)

class Career(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(40), nullable=False)
     date = db.Column(db.String(30), nullable=False)
     title = db.Column(db.String(80), nullable=False)
     desc = db.Column(db.Text, nullable=False)
     place = db.Column(db.String(40), nullable=False)
     site = db.Column(db.String(50), nullable=True)







