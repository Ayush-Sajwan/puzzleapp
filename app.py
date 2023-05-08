from flask import Flask,render_template,request,make_response,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key='This is a Puzzle'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users.db"


db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    progress=db.Column(db.Integer)

#this will render the main page
@app.route('/')
def mainpage():
    return render_template("login.html")

#this will login and render intro page
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form['user']
        email=request.form['email']
        password=request.form['password']


        if check(email):
            
            user=User.query.filter_by(email=email).first()

            if user.name==name:
                if user.password==password:
                     resp=make_response(render_template('intro.html',namep=name))
                     resp.set_cookie('email',email)
                     return resp
                else:
                     flash("Email is already Registered Use Your Old Username and Password")
                     return redirect('/')
            else:
                 flash("Email is already Registered Use Your Old Username and Password")
                 return redirect('/')
        
        else:
             user=User(name=name,email=email,password=password,progress=0)
             db.session.add(user)
             db.session.commit()

             resp=make_response(render_template('intro.html',namep=name))
             resp.set_cookie('email',email)
             return resp
                    

            
#function to check whether a email is present or not in the database
def check(email):

    user=User.query.filter_by(email=email).first()

    if user:
        return True
    else:
        return False

#this route will render the page which conatins about info of nobita
@app.route('/about')
def about():
    return render_template("nobitaabout.html")

#this route will render the page for breakfast 
@app.route('/breakfast',methods=['GET','POST'])
def breakfast():
    email=request.cookies.get('email')

    user=User.query.filter(User.email==email).first()
    user.progress=2
    name=user.name
    db.session.commit()

    return render_template("breakfast.html",namep=name)

#this route will render the page for tvshow
@app.route('/tvshow',methods=['GET','POST'])
def tvshow():
    email=request.cookies.get('email')

    user=User.query.filter(User.email==email).first()
    user.progress=3
    name=user.name
    db.session.commit()

    return render_template("tvshow.html",namep=name)

#route for clue 1 of tvshow page
@app.route('/tvshowClue1')
def tvClue1():
    return render_template('tvshowClue1.html')
#route for clue 2 of tvshow page
@app.route('/tvshowClue2')
def tvClue2():
    return render_template('tvshowClue2.html')


#this route will render the page for university
@app.route('/university',methods=['GET','POST'])
def university():
    email=request.cookies.get('email')

    user=User.query.filter(User.email==email).first()
    user.progress=4
    name=user.name
    db.session.commit()

    return render_template("university.html",namep=name)


#this route will render the page for home
@app.route('/home',methods=['GET','POST'])
def home():
    email=request.cookies.get('email')

    user=User.query.filter(User.email==email).first()
    user.progress=5
    name=user.name
    db.session.commit()

    return render_template("home.html",namep=name)

#this is route for finish page
@app.route('/finished')
def finish():
    return render_template("finished.html")


@app.route('/adminAuth',methods=['GET','POST'])
def auth():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']

        if  email == "ayushsajwan19@gmail.com" and password == "RSia+1":
            progress=User.query.all()
            return render_template('admin.html',allUser=progress)
        else:
            flash("Wrong Id And Password")
            return redirect('/adminAuth')
    
    return render_template('adminAuth.html')



'''
@app.route('/admin')
def admin():
    progress=User.query.all()
    return render_template('admin.html',allUser=progress)
'''

@app.route('/delete/<int:id>')
def delete(id):
    user=User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/adminAuth')


if __name__=="__main__":
    app.run(debug=True)