# Bet Goals

Bet Goals is an app I created during my time as an Insight fellow to use soccer and betting related data to predict the result of matches in the English Premier League and identify which games to bet on. The English Premier League is watched by an audience of 1.35 billion people every year and around a billion pounds are bet on games every year. In this project we identify and exploit systemic inefficiencies in the bookmakers odds.

**Link to web app:** https://betgoals.herokuapp.com/ \
**Link to presentation:** https://docs.google.com/presentation/d/1jJrTCnUXaHHfAmipQfUcQZxc6jPEwkKBx4CbW67AeO4/edit#slide=id.g8a6bea1bd9_0_53


## Project Description
***
### Motivation
In the past 4 years, the bookmakers odds have always favoured either the home team or the away team. Not a single game has been backed by the bookmaker to end in a draw in this time frame.\ 
![Draws_EDA](/Images/bookies_fav2.png =100x80)

In this same time span, around 25% of the games have ended in a draw.\
![Results](/Images/Results.png)

This systematic underestimation of the chances of a game ending in a draw lets the bookmaker overestimate the chances of a home win. Thus predicting draws precisely is the key to building a profitable betting strategy. To do this, we built a model that can identify draws with 36% precision. Even though this means we will be wrong 2 out of 3 times, the odds on draws have historically been high enough to give us around 20% return on investment.

### File Structure
**Images folder:**-  Contains the images generated through EDA, modelling and model evaluation.\
**Data folder:**-  Contains all the data used in the project.
**Bet_Goals.py**- The streamlit-based app delpoyed on Heroku.
**Data Cleaning.ipynb**-The Jupyter notebook that deals with cleaning and organizing data obtained from different sources.
**Multiple All vs One Classification**- The Jupyter notebook that contains the logistic regression models and betting strategy optimization.

## Modelling
***
### Data Sources and Feature Engineering
The data for this project was obtained from multiple sources online. We considered betting and match results data from the last 5 years. Betting data was downloaded from **oddsportal.com**, team performance data was downloaded from **fbref.com** and the result of every match in the english premier league over the last five years was obtained from **football-data.co.uk**.

### Model
The model was built in Python using pandas and scikit-learn libraries heavily. I built three one-vs-all classifiers, where the first classifier predicts the chances of the game ending in a draw, the second classifier focusses on the chances of the game ending in a home win and the third on the chances of the game ending in an away win. 

### Model Evaluation
The most important performance measure for our model is its accuracy in predicting draws. We compare the precision of our model with the baseline model of backing the bookmaker's favourite to win everytime.
![Model_performance](/Images/model_performance.png)\

We can see that our model is 36% more precise in predicting draws as compared to the baseline model. \

### Feature Importance
As expected, the three most important features for the model are the bookmakers odds for each of the three possible results. The fourth most important feature is the difference in points accumulated by the teams last season. This is a measure of difference between the home team and away team's performance last season.
![Draw_features](/Images/Feature_importance_draw.png)

### Betting Strategy Evaluation
I evaluated three possible betting strategies:\
![Money](/Images/money_made.png)
* The baseline strategy (I) was to bet on the bookmaker's favourite on every game so far this season (286 games). This strategy would have resulted in us losing around 6% of our money so far this season. 
* The second strategy (II) was to bet on every game and on the winner predicted by our model (286 games). Using this strategy would have resulted in us breaking even on our investment so far.
* The third strategy (III) was to bet only on games the classifier predicts will end in a draw (69 games). This strategy would have resulted in us making a 22% return on our investments so far this season.

## Contact
***
You can reach me in the following ways:
**Email:** sureshr14@gmail.com \
**LinkedIn:** https://www.linkedin.com/in/sureshr14/ 
