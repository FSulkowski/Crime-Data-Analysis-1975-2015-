from flask import Flask, jsonify, render_template
import pandas as pd

merged_df = pd.read_csv("Resources/merged_data.csv")

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


@app.route('/heatmap')
def prop4():
    # Convert the DataFrame to JSON
    data_json = merged_df.to_json(orient='records')
    print(data_json)  # Log the data for debugging

    # Get unique years for the dropdown
    unique_years = merged_df['report_year'].unique()

    return render_template('heatmap.html', data=data_json, years=unique_years)

@app.route('/update_map/<int:year>')
def update_map(year):
    # Prepare data for the heatmap for the selected year
    filtered_data = merged_df[merged_df['report_year'] == year]
    heat_data = [[row['Latitude'], row['Longitude'], row['crimes_percapita']] 
                  for index, row in filtered_data.iterrows()]

    # Return the heat data as JSON
    return jsonify({'heat_data': heat_data})

@app.route('/view_map/<int:year>')
def view_map(year):
    # Serve the generated heatmap HTML file
    map_file = f'crime_heatmap_{year}.html'
    return render_template('view_map.html', map_file=map_file)


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
