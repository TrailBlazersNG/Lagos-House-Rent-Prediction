# Lagos House Rent Prediction
### By Kehinde Olalekan, Babajide Alao, Onabanjo Micheal, Paul Adegbite, Innocent Alinta
#### Statement of Purpose
##### Knowing the rate of inflation in the country at the moment, one needs to be well-informed or kept abreast of the rent prices of properties in various locations in Lagos state, Nigeria.With this project, the aim is to build a model that helps users to predict the rent price of properties in their chosen locations across Lagos State, Nigeria.
#### Data Description
##### The data used in the course of this project was scraped from a real estate website. The scraped data contains over 141,000 observations and 7 features.
#### Repository Files
##### The following is a detailed description of the files in the repository.
- Data cleaning - Jupyter notebook of the cleaning process
- Data Scraping - Jupyter notebook of the web scraping process using Beautiful Soup
- Data Wrangling - EDA - Jupyter notebook containing visuals and analysis done on the dataset
- Machine Learning Prediction - Jupyter notebook of the machine learning model
- final_xgboost_model - Pickle file of the machine learning model used in creation of the streamlit app
- model_data.csv - Csv file after cleaning of the dataset
- newhousing.csv - Csv file of the observation scaped from the website using Beautiful Soup
- newlagosrent.csv - Csv file after the scraped file was first cleaned using Microsoft Excel
- app.py - Pyhton file used to create the streamlit app
#### Tools
- Beautiful Soup for Scraping of the data
- Pandas for Accessing and manipulation of the data
- Matplotlib and Seaborn for Visualization and generating insights
- XGBoost for creating a gradient-boosted regression model.
- Streamlit for creating a frontend application
- Microsoft Excel For initial stage of data cleaning
