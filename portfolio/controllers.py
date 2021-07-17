import re
from typing import Protocol
from flask.helpers import flash
from portfolio import app, os, db
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from portfolio.models import Profile, Project, Blog, Contact
from portfolio.forms import ContactForm

@app.route('/', methods=['POST', 'GET'])
def index():
    profile = Profile.query.all()
    project = Project.query.all()
    blog = Blog.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('app/index.html', profile=profile, blog=blog, project=project, form=form)

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


# Project Section =========================

@app.route('/admin/project')
def project():
    project = Project.query.all() 
    return render_template('admin/project.html', project=project)

@app.route('/admin/project-add', methods=['GET', 'POST'])
def project_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        project = Project(
            name = request.form['name'],
            tag = request.form['tag'],
            tech = request.form['tech'],
            desc = request.form['desc'],
            info = request.form['info'],
            link = request.form['link'],
            image = filename
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('project'))
    return render_template('admin/project-add.html')

@app.route('/admin/project-update/<int:id>', methods=['GET', 'POST'])
def project_update(id):
    project = Project.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        project.name = request.form['name']
        project.tag = request.form['tag']
        project.tech = request.form['tech']
        project.desc = request.form['desc']
        project.info = request.form['info']
        project.link = request.form['link']
        project.image = filename
        db.session.commit()
        return redirect(url_for('project'))
    return render_template('admin/project-update.html', project=project)


@app.route('/admin/project-delete/<int:id>', methods=['GET', 'POST'])
def project_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('project'))

# Blog Section =========================

@app.route('/admin/blog')
def blog():
    blog = Blog.query.all() 
    return render_template('admin/blog.html', blog=blog)

@app.route('/admin/blog-add', methods=['GET', 'POST'])
def blog_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            name = request.form['name'],
            desc = request.form['desc'],
            link = request.form['link'],
            image = filename
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('admin/blog-add.html')

@app.route('/admin/blog-update/<int:id>', methods=['GET', 'POST'])
def blog_update(id):
    blog = Blog.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog.name = request.form['name']
        blog.desc = request.form['desc']
        blog.link = request.form['link']
        blog.image = filename
        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('admin/blog-update.html', blog=blog)


@app.route('/admin/blog-delete/<int:id>', methods=['GET', 'POST'])
def blog_delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog'))

# Contact Section =========================

@app.route('/admin/contact')
def contact():
    contact = Contact.query.all()
    return render_template ('admin/contact.html', contact=contact)

@app.route('/admin/contact-delete/<int:id>', methods=['GET', 'POST'])
def contact_delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contact'))