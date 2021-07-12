import re
from flask.helpers import flash
from portfolio import app, os, db
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from portfolio.models import Profile
# from portfolio.forms import 

@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/admin/profile', methods=['GET', 'POST'])
def profile():
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
    return render_template('admin/profile.html')