from flask import Flask
from flask import render_template 
from flask import url_for
from flask import redirect
from flask import abort
from cash import navbar, links_one, links_two

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html', 
  title = 'index', navbar = navbar, 
  links_one = links_one, 
  links_two = links_two)

@app.route('/google.com')
def google():
  return redirect("http://www.google.com")
 
@app.route('/twitter.com')
def twitter():
  return redirect("http://www.twitter.com")

@app.route('/facebook.com')
def facebook():
  return redirect("http://www.facebook.com")

@app.route('/get-in-touch')
def get_in_touch():
  return render_template('get_in_touch.html', 
  links_one = links_one, 
  links_two = links_two)

@app.route('/<link>')
def links(link):
  checklist = links_one + links_two
  if link in checklist:
    return 'it is work'
  else:
    abort(404)
    return 404

app.run(debug = True, host='0.0.0.0', port=8080)

with app.test_request_context():
  for item in links_one:
    print(url_for('links',link = item))
    print(item)

