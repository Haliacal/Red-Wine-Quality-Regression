# Red Wine Quality Classifier

## Project Overview

Using a Red Wine Kaggle Data, I tried to classify the the quality of the wine based on its physiochemical components. This includes, but is not limited to, Alcohol, Density, Acidity, PH, etc. I analysing and cleaning the data allowed me to train a model (Random Forest) to use within a flask server. This is then called by a html website with CSS and jQuery by inputting the features on the website itself.
### Table of Contents

- [Dataset](#dataset)
- [Project Phases](#project-phases)
  - [Phase 0 - Research](#phase-0---research)
  - [Phase 1 - Data Collection and Pre-processing](#phase-1---data-collection-and-pre-processing)
  - [Phase 2 - Model](#phase-2---model)
  - [Phase 3 - Model Evaluation and Refinement](#phase-3---model-evaluation-and-refinement)
  - [Phase 4 - API Endpoint](#phase-5---API-Endpoint)
  - [Phase 5 - React Website](#phase-5---React-Website)
  - [Phase 6 - Mobile App](#phase-6---Mobile-App)
  - [Phase 7 - Further Work](#phase-7---further-work)
- [Languages](#Languages)
- [Packages](#Packages)

## Dataset

The dataset used in this project can be found [here](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009). Performing an EDA on the dataset revealed that the data is very skewed. The quality class is also underrepresented and there are multiple features that have multicollinearity. Despite that I cleaned the data as best I could to a high enough degree to train a model but for a proper deployment there will need to be more data that also represents the other classes. This is because the quality labels are over presented in ratings 5-6, underrepresented in ratings 3-4 and 7-8, and not represented in ratings 1-2 and 9-10.   
## Project Phases

### Phase 1 - Data Collection and Pre-processing

- Download the dataset.
- Explore the dataset.
- Pre-process the data.

Creating a correlation matrix it was easy to see any obvious correlations between the features. Some noticeable ones were (+)Alcohol and Quality, (+)PH and Fixed Acidity, and (-)Alcohol and Density. Getting the VIF confirmed that Density and  and Fixed acidity had multilinearity. Thus they had to be removed.

I also removed any outlies that were in the data. This was done on the basis if the point was more than 3 s.d away. I used a box plot to detect if there were any outlies present in the first place.
### Phase 2 - Model

- Data Splitting 
- Training

I split the data in training and test sets and started training a logistic regression model. This turned out to have an accuracy of 60% Which is a decent start but I wanted to do better.  
### Phase 3 - Model Evaluation and Refinement

- Grid Search CV
- Hyper parameter Tuning 

I used a grid search cross validation method to evaluate 3 different models and there best parameters. This included Logistic Regression, Naïve bayes and Random Forest Classifier.
In the end the Random forest won with accuracy of ~70%.  This lower than I though but it is understandable as the data classes are unbalanced. Have an ensemble with help with this unbalance and is the reason why I think it won in turn of accuracy.
### Phase 4 - Flask Server

- Flask
- Postman

Pickling the model we can save it in a local directory and load it into a flask server. Creating a POST function we can send the inputs for the model to estimate the quality. This was tested using the Postman software.
### Phase 5 - HTML Website

- Html
- Requests
- JSON

Creating the HTML website we can give users textboxes to input their data. We can send a request to the flask server and receive a JSON file response and access the information to output in the main body of the Website.
### Phase 6 - AWS
- TBC
### Phase 7 - Further Work

- Limits for inputs
- Warning messages.
## Languages

- Python
- Jupyter Notebook
- HTML, CSS, jQuery 
## Packages

Main packages:
- Numpy
- Pandas
- Sklearn
- Matplotlib, Seaborn
- Stats models
- Pickle
- Flask