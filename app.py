from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = "random string"
db=SQLAlchemy(app)

class users(db.Model):
    id=db.Column('user_id', db.Integer, primary_key=True)
    name=db.Column(db.String(128))
    password=db.Column(db.String(256))
    mark=db.Column(db.Integer)

    def __init__(self, name, password,mark=0):
        self.name=name
        self.password=password
        self.mark=mark

@app.route('/')
def show_all():
   return render_template('show_users.html', users = users.query.all() )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            user = users(request.form['name'],
                               request.form['password'])

            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
