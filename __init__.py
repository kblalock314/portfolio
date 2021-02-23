from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email, Length
from wtforms import validators, StringField, SubmitField, TextAreaField
from config import mail_username, mail_password
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '45349dsf0843bjh34508nkj453'

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")        

@app.route("/godaddy-split-test")
def godaddy():
    return render_template("godaddy-split-test.html")       

@app.route("/module-prototype")
def flexbox():
    return render_template("module-prototype.html")    

@app.route("/valley-chevy-content-strategy")
def valleychevy():
    return render_template("valley-chevy-content-strategy.html")   

@app.route("/recruiting-content-strategy")
def rcs():
    return render_template("recruiting-content-strategy.html")        

@app.route("/modules")
def modules():
    return render_template("modules.html")   

@app.route("/empathy-mapping")
def mapping():
    return render_template("empathy-mapping.html")   

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        message = request.form.get('message')

        msg = Message(
            subject=('Website email from ' + name), body=('Email address: '+ email + '\nMessage: ' + message), sender=mail_username, recipients=['katieblalock314@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", form=form, success=True)   
    return render_template("contact.html", form=form)    

@app.route("/token-creator", methods=["POST", "GET"])
def tokens():
    if request.method == "POST":
        url = request.form["response"]
        validurls = ["godaddy.com", "http://www.godaddy.com", "http://godaddy.com", "http://godaddy.com/",
                     "https://www.godaddy.com/", "https://www.godaddy.com", "www.godaddy.com", "www.godaddy.com/"]

        if url in validurls:
            flash('Your token is:')
            flash('[@T[link:<relative path=""/>]@T]')

        else:
            for c in validurls:
                if c in url:
                    link = url.split('.com/')
                    path = link[1]
                    start = '[@T[link:<relative path="'
                    end = '"/>]@T]'
                    x = start + path + end
                    flash('Your token is:')
                    flash(x)
                    break
                else:
                    flash("Please enter a valid en-US link")
                    break

    return render_template("token-creator.html")       

if __name__ == "__main__":
    app.run(debug=True)
