from flask import Flask, render_template,request,redirect,url_for
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

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))


if __name__=="__main__":
    app.run(debug=True, use_reloader=False)