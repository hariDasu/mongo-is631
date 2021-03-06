from flask import Flask,request,render_template
from flask_bootstrap import Bootstrap
import backend

def createApp():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app=createApp();

@app.route("/")
def test():
    return render_template('mongoZips.html')

@app.route("/query1")
def query1():
    results = backend.query1();
    print results
    return results


@app.route("/query2")
def query2():
    results = backend.query2();
    print results
    return results


@app.route("/query3")
def query3():
    results = backend.query3();
    print results
    return results

@app.route("/query4")
def query4():
    results = backend.query4();
    print results
    return results

@app.route("/mongoEmps")
def emps():
	return render_template('mongoEmps.html')

@app.route("/empQuery1")
def empsQuery1():
    results = backend.empsQuery1();
    print results
    return results

@app.route("/empsQuery2")
def empsQuery2():
    results = backend.empsQuery2();
    print results
    return results


@app.route("/empsQuery3")
def empsQuery3():
    results = backend.empsQuery3();
    print results
    return results


@app.route("/empsQuery4")
def empsQuery4():
    results = backend.empsQuery4();
    print results
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

