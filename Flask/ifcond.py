from flask import Flask, render_template
"""Getting the instance of Flask application for WSGI"""
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to result web page </H1></html>"

@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result2.html",results=score)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)