from flask import Flask, jsonify, render_template
import pandas as pd
import os




merged_df = pd.read_csv("Resources/merged_data.csv")



app = Flask(__name__, 
            static_folder='static', 
            template_folder='templates')


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
