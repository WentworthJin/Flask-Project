from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User, Post
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from datetime import datetime
from app.forms import EditProfileForm

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/Setup')
def setup():
    return render_template('Set_Up.html')   

@app.route('/Grammar')
def grammar():
    return render_template('grammar.html')  

@app.route('/Math')
def math():
    return render_template('math.html')  

@app.route('/Condition')
def condition():
    return render_template('condition.html')  

@app.route('/Function')
def function():
    return render_template('function.html') 

@app.route('/Class')
def classhtml():
    return render_template('class.html') 

@app.route('/Gener')
def genertic():
    return render_template('generic.html') 

@app.route('/Inher')
def inhert():
    return render_template('inher.html') 

@app.route('/Test', methods=['GET','POST'])
@login_required
def test():
    name = current_user.username
    currentid = current_user.id
    mark = Post.query.filter_by(user_id=current_user.id).first()
    result = mark.Mark
    Record = None
    today = datetime.now()
    CurrentResult = 0
    feedbackl=""
    if request.method == 'POST':
        First = request.form.getlist('question-1-answers')
        Second = request.form.getlist('question-2-answers')
        Third = request.form.getlist('question-3-answers')
        Fourth = request.form.getlist('question-4-answers')
        Fifth = request.form.getlist('question-5-answers')
        Six = request.form.getlist('question-6-answers')
        Seven = request.form.getlist('question-7-answers')
        Eight = request.form.getlist('question-8-answers')
        Nine = request.form.getlist('question-9-answers')
        Ten = request.form.getlist('question-0-answers')
        if 'A' in First:
           CurrentResult+=10
        else:
            feedbackl + "You should review the first chapter " 

        if 'C' in Second:
           CurrentResult+=10
        if 'A' in Third:
           CurrentResult+=10
        if 'D' in Fourth:
           CurrentResult+=10
        if 'B' in Fifth:
           CurrentResult+=10
        if 'B' in Six:
           CurrentResult+=10
        if 'D' in Seven:
           CurrentResult+=10
        if 'A' in Eight:
           CurrentResult+=10
        if 'C' in Nine:
           CurrentResult+=10
        if 'C' in Ten:
           CurrentResult+=10
        Record = Post(Mark=CurrentResult, Finish_Time=today, Feedback=feedbackl, user_id=currentid)
        db.session.add(Record)
        db.session.commit()
        flash("Congraulations, You have finished the test. Check your result in your Profile!")
        return render_template('home.html')
    return render_template('Testbase.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You have successfully login!')
        return homepage()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('You have successfully login!')
        return homepage()
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logout!")
    return homepage()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You already login!')
        return homepage()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered Swift Learner!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    list=[]
    average = 0
    user = User.query.filter_by(username=username).first_or_404()
    mark=Post.query.filter_by(user_id=user.id)[-1]
    allmark=Post.query.filter_by(user_id=user.id).all()
    all=Post.query.all()
    for i in allmark:
        list.append(i.Mark)
    for i in list:
        average+=int(i)
    average=average/len(list)
    average=int(average)
    return render_template('user.html', user=user, mark=mark, all=all,average=average, allmark=allmark)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your profile have been saved.')
        return redirect( url_for('user', username=current_user.username) )
    elif request.method == 'GET':
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

if __name__=='__main__':
    app.run(debug=True)