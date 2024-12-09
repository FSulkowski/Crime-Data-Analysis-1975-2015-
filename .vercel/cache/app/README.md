**40-Year Crime and Safety Analysis of U.S. Cities**

This project analyzes 40 years of crime and safety trends across U.S. cities (1975-2015). It explores patterns and factors impacting crime rates, visualizing data through interactive maps and line graphs.


**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Data Sources](#datasources)

**Installation**

***How to install project***
1. Clone the repository.
    ```bash
    git clone https://github.com/Jessiii929/project_3.git

2. Navigate into the project directory.
    ```bash
    cd project3
 
3. Install dependencies.
    ```bash
   pip install seaborn ipywidgets folium IPython.display psycopg2

**Usage**

Instructions on how to use the project:
After running `python proj3.py`, an interactive web page will launch, where you can explore different visualizations, including heat maps and line graphs, based on the crime data.
  
**Features**

***Heat Map***
- Interactive heat map using Folium to visualize crime rates across U.S. cities.
- Dropdown feature to filter crime data by year, providing a year-by-year view of crime rates.

***Seaborn Line Graph***
- Line graphs for each city showing crime trends over time.
- Dropdown filter to isolate data for individual cities for in-depth analysis.

***Folium Crime Index Map***
- Crime index map highlighting the top 5 safest cities.
- Legend showing average crime rate per city, helping users understand relative safety.

***Flask Server***
- Integrates various HTML files to create an interactive web application, bringing together visualizations and data.

**Data Sources**

The crime data for this project was sourced from [Kaggle](https://www.kaggle.com/), where a CSV file with detailed crime statistics was obtained. The original data is from the FBI's Uniform Crime Reporting (UCR) program, specifically the "Offenses Known and Clearances by Arrest" database. Maintained by the National Archives of Criminal Justice Data, this dataset provides a comprehensive view of crime trends across various U.S. cities, enabling in-depth analysis and insights into historical crime and safety patterns.

