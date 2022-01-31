from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from config import navbar, links_one, links_two

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html',
                           title='index', navbar=navbar,
                           links_one=links_one,
                           links_two=links_two)


@app.route('/google.com')
def google():
    return redirect("http://www.google.com")


@app.route('/twitter.com')
def twitter():
    return redirect("http://www.twitter.com")


@app.route('/facebook.com')
def facebook():
    return redirect("http://www.facebook.com")


@app.route('/get_in_touch',methods = ["POST", "GET"])
def get_in_touch():
    if request.method == 'POST':
        print(request.form)
    return render_template('get_in_touch.html',
                           navbar=navbar,
                           links_one=links_one,
                           links_two=links_two)


@app.route('/singup', methods = ['POST', 'GET'])
def sing_up():
    if request.method == 'POST':
        print(request.form)
    return render_template('singup.html',
                           navbar=navbar,
                           links_one=links_one,
                           links_two=links_two)


@app.route('/login', methods = ['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        print(request.form)
    return render_template('login.html',
                           navbar=navbar,
                           links_one=links_one,
                           links_two=links_two)


@app.route('/<link>')
def links(link):
    checklist = links_one + links_two
    if link == 'blog':
        return log_in()
    else:
        return render_template('404.html'), 404


app.run(debug=True, host='0.0.0.0', port=8080)
