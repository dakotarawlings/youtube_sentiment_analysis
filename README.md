# YouTube Comments Sentiment Estimator

<p align="center">
  <img src="readme_images/homepage.png" width="600" >
</p>

### Web App Link: https://youtube-sentiment-estimator.herokuapp.com/

## Overview
* Scraped live and historical timeseries weather data from NOAA bouy stations
* Deployed model in a full stack web app

## Resources
**Python version:** 3.8

**Packages:** Spacy, sqlite3, pandas, numpy, sklearn, XGBoost, SVA, seaborn, requests, flask, pickle

**Languages:** python, MYSQL, AWS, EC2, amazon RDS, SQLite, JavaScript, HTML, CSS

## Data Cleaning and Feature Engineering
* Used the IMDB movie review sentiment database for training 
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews 
* Used word2vec and spacy word embedding model
* Calculated vector for each document (comment) by averaging word embeddings for all words in a document
 
## Model Development
* Split the data into train and test sets (20% test) with the document sentiment (positive or negative) as the target value
* Due to the high dimensionality of the dataset, I tested random forest, XGB, SVC, and Lasso models 
* Selected the SVC model as the model for productionalization
  
## Model performance
The SVC model achieved an accuracy of 87% for predicting the sentiment (positive or negative)

## Model Productionalization

* Used Youtube Comments API to automatically retrieve a list of comment strings for a given link
* Calculate word embeddings for each comment for a given video
* Implement SVC model to predict sentiment of each comment
* Calculate the percentage of comments that have a positive sentiment
* Created flask API endpoint 
* Wrote a full stack web application in HTML, CSS, and JavaScript 

## Future work
* Working on improving documentation
* Improved error handling in the web app and the API
