# German Credit Risk

The dataset was imported from Kaggle.

It contains multiple features that might affect the risk score of a german citizen. 


The steps taken to clean, explore, preprocess and test the models are outlines below:



1. Data was preprocessed by assigning categories instead of objects.


2. EDA.

We will be exploring the features of the dataset to see if some of them are correlated.

Numerical features and Risk.

Target variable Risk is:

- weakly related with Credit Score (according to the boxplot Risk and Credit).
- weakly related with Age (according to BoxPlot).
- moderately related with Duration of Credit (according to boxplot).

Categorical features and Risk.

Target variable Target is:

- strongly related with Sex. Males seem to have a lower risk when taking a credit.
- strongly related with Housing. People that own a house are less risky when taking a credit.
- Most of the clients take car and radio / tv loans. Most of the risk is lower, however comparing to other categories, the car and radio bars have also a higher number of loans with risk.

Tip: boxplots for numerical fetures. countplots for categorical ones.


Correlation matrix. Checking if the predicted correlations are true.

Positive correlation between duration and credit amount. Consequently, we will exclude the duration.

Feature importance in the Random Forest:

Using the feature importance attribute, the following features have a higher influence on the target variable:

credit, age, duration.

Feature importance in the Logistic Regression:

- Radio/TV purpose has a lower risk. However, the vacation feature increases the risk.

- Duration influences negatively the risk, while if the customer has a house, the risk is lower.