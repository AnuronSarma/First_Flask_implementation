from flask import Flask, render_template
"""Getting the instance of Flask application for WSGI"""
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to result web page </H1></html>"

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'Score':score,'result':res}
    return render_template("result1.html",results=exp)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)