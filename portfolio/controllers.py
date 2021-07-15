import re
from flask.helpers import flash
from portfolio import app, os, db
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from portfolio.models import Profile, Education, Career, Contact
# from portfolio.forms import 

@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')


# Profile Info =========================

@app.route('/admin/profile')
def profile():
    profile = Profile.query.all() 
    return render_template('admin/profile.html', profile=profile)

@app.route('/admin/profile-add', methods=['GET', 'POST'])
def profile_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        profile = Profile(
            name = request.form['name'],
            age = request.form['age'],
            location = request.form['location'],
            desc = request.form['desc'],
            image = filename
        )
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('admin/profile-add.html')

@app.route('/admin/profile-update/<int:id>', methods=['GET', 'POST'])
def profile_update(id):
    profile = Profile.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        profile.name = request.form['name']
        profile.age = request.form['age']
        profile.location = request.form['location']
        profile.desc = request.form['desc']
        profile.image = filename
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('admin/profile-update.html', profile=profile)