from flask import Flask, render_template
"""Getting the instance of Flask application for WSGI"""
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to flask web page using html tags</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
