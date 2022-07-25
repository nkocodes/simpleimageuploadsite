from flask import Flask, render_template, request, redirect, url_for
import os

path= os.path.dirname(__file__)
start = str(path)
start = start.replace("\\", "/")
directory = "/static/user_files/"

app = Flask (__name__)
app.secret_key = 'supersecretappkey!!!'



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/your-url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        f = request.files['file']
        full_name = request.form['code']
        f.save(f"{start}{directory}" + full_name + ".jpg")
        return render_template("your_url.html", code=request.form['code'])             
    else:
        return redirect(url_for('home'))
    
@app.route('/<string:code>')
def redirect_to_url(code):
    return redirect (url_for('static', filename='user_files/' + code +".jpg"))


