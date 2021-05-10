from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
def homepage():
    return render_template('home_page_v-2.html')

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

@app.route('/Test')
def test():
    return render_template('Testbase.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index')) # Redirect to main page #
    return render_template('login.html', title='Sign In', form=form)

if __name__=='__main__':
    app.run(debug=True)