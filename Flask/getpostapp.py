from flask import Flask, render_template, request
"""Getting the instance of Flask application for WSGI"""
app=Flask(__name__)

@app.route("/")
def welcome():
    print("Home route accessed")  # Print to debug
    return "Welcome to my flask home page"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello! {name}'
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello! {name}'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)