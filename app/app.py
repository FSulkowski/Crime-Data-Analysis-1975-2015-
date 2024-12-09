from flask import Flask, jsonify, render_template
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def prop1():
    
    return render_template('index.html')


@app.route("/data") 
def prop2(): 
    return render_template('data.html')

@app.route("/visualizations")
def prop3():
    return render_template('visualizations.html')




@app.route("/safest_cities")
def prop5():
    return render_template('safety.html')

@app.route("/city_specific_crime")
def prop6():
    return render_template('city_specific_crime.html')

@app.route("/analysis")
def prop7():
    return render_template('analysis.html')

@app.route("/Code")
def prop8():
    return render_template('code_snippets.html')

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  # Get port from environment variable or default to 5000
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0 for all IPs on the assigned port
