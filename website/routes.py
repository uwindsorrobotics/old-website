from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import ProjectForm, Login
from website.models import Project, User
from flask_login import login_user, current_user, logout_user, login_required

# from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and form.password.data==user.password:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(author=form.author.data, title=form.title.data, content=form.content.data)
        db.session.add(project)
        db.session.commit()
        flash(f'Created project {form.title.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('new.html', form=form, legend='New Project')

@app.route('/<project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm()
    if form.validate_on_submit():
        project.title = form.title.data
        project.content = form.content.data
        project.author = form.author.data
        db.session.commit()
        flash('Successfully updated project!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = project.title
        form.author.data = project.author
        form.content.data = project.content        
    return render_template('new.html', form=form, legend='Update Project')

@app.route('/<project_id>/delete', methods=['GET', 'POST'])
def delete(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Successfully deleted project!', 'success')
    return redirect(url_for('home'))