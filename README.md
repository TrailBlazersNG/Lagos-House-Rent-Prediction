{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "71034cea-f161-4f93-bc42-43bdcf534888",
   "metadata": {},
   "source": [
    "# Lagos House Rent Prediction"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3220813d-da59-4b31-96f8-1b8677542de5",
   "metadata": {},
   "source": [
    "### By Kehinde Olalekan, Babajide Alao, Onabanjo Micheal, Paul Adegbite, Innocent Alinta"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "921b1149-d377-44e7-885e-a58a7d42c272",
   "metadata": {},
   "source": [
    "#### Statement of Purpose"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca745f76-3c33-4766-9b27-47239d8ce82c",
   "metadata": {},
   "source": [
    "##### Knowing the rate of inflation in the country at the moment, one needs to be well-informed or kept abreast of the rent prices of properties in various locations in Lagos state, Nigeria.With this project, the aim is to build a model that helps users to predict the rent price of properties in their chosen locations across Lagos State, Nigeria."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f22a33d9-3382-42e9-a29b-896f8d807817",
   "metadata": {},
   "source": [
    "#### Data Description"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48cf9446-6221-46b9-9776-dc525dd72f1e",
   "metadata": {},
   "source": [
    "##### The data used in the course of this project was scraped from a real estate website. The scraped data contains over 141,000 observations and 7 features."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7dc1bf5-9579-445a-8781-69eef5786a57",
   "metadata": {},
   "source": [
    "#### Repository Files"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37427caf-6f56-4eb0-a4d7-154f8f62d75f",
   "metadata": {},
   "source": [
    "##### The following is a detailed description of the files in the repository.\n",
    "- Data cleaning - Jupyter notebook of the cleaning process\n",
    "- Data Scraping - Jupyter notebook of the web scraping process using Beautiful Soup\n",
    "- Data Wrangling - EDA - Jupyter notebook containing visuals and analysis done on the dataset\n",
    "- Machine Learning Prediction - Jupyter notebook of the machine learning model\n",
    "- final_xgboost_model - Pickle file of the machine learning model used in creation of the streamlit app\n",
    "- model_data.csv - Csv file after cleaning of the dataset\n",
    "- newhousing.csv - Csv file of the observation scaped from the website using Beautiful Soup\n",
    "- newlagosrent.csv - Csv file after the scraped file was first cleaned using Microsoft Excel\n",
    "- app.py - Pyhton file used to create the streamlit app"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0642660-b41d-4466-87d1-01364110e3e9",
   "metadata": {},
   "source": [
    "#### Tools"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d927606-3219-45e8-aba8-673db5f12df0",
   "metadata": {},
   "source": [
    "- Beautiful Soup for Scraping of the data\n",
    "- Pandas for Accessing and manipulation of the data\n",
    "- Matplotlib and Seaborn for Visualization and generating insights\n",
    "- XGBoost for creating a gradient-boosted regression model.\n",
    "- Streamlit for creating a frontend application\n",
    "- Microsoft Excel For initial stage of data cleaning"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
