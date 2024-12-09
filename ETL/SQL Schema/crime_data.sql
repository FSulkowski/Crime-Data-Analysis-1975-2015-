DROP TABLE crime_data

CREATE TABLE crime_data (
id SERIAL PRIMARY KEY,
report_year INTEGER,
agency_code VARCHAR(255),
agency_jurisdiction VARCHAR(255),
population FLOAT,
violent_crimes FLOAT,
homicides FLOAT,
rapes FLOAT,
assaults FLOAT,
robberies FLOAT,
months_reported FLOAT,
crimes_percapita FLOAT,
homicides_percapita FLOAT,
rapes_percapita FLOAT,
assaults_percapita FLOAT,
robberies_percapita FLOAT
);

SELECT * FROM crime_data;