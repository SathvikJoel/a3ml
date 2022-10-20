[Link to source Github](https://github.com/abhishekkrthakur/approachingalmost)

# Chapter 1: Introduction

* Supervised setting vs unsupervised setting

* Superviseed setting can be further divided into classification and regression

files associated : t-SNE.ipynb

# Chapter 2: Cross Validation

> Def: Cross validation is a step in the process of building machine learning model which helps us ensure our model fits the data accurately and is not overfitting 


* There are a lot of differnt types of cross calidation techniques

* Choice depends in the dataset

Types of Cross Validation:

* K-fold cross validation
* Stratified K-fold cross validation
* Holdout cross validation
* leave one out cross validation
* group k-fold cross validation

## K Fold and Stratified K Fold

* Divide the dataset into k folds

* Train the model on k -1 folds and test on the remaining fold

* Repeat this process k times, from scratch each time

* Average the results

* Stratified K fold is used when the dataset is imbalanced

* Stratified K fold divides the dataset into k folds in such a way that the proportion of each class is same in each fold

### Note :

* For Regression problems, stratified K fold is not used

* But still observe the distribution of the target variable and if its imbalanced, use stratified K fold by dividing the target variable into bins

* For the number of bins, use the Sturges Rule

Number of bins = $1 + {log_2(n)}$

## Holdout Cross Validation

* Divide the dataset into two parts, training and testing

* Train the model on the training set and test on the testing set

* Done !

### Caution :

Holdout cross validation might not be a good measure as it highly relies on the random split of the dataset. It is also not a good measure when the dataset is small.

## Leave One Out Cross Validation

K fold with k = n, do it only when the dataset is small

## Group K Fold Cross Validation

Data is considered as groups, and each group is assigned to a fold, you can decide which datapoints form a group

This is used when we should not be seeing somedata points that we have seen in training during testing phase.

> Its very important to decide on the cross validation technique before starting the project, to create a more robust model

For eg, if there are pictures of cancer patients, we should make sure that the pictures of same patient doesn't apprear in both training and testing set. So, a careful staraegy should be used to split the data into training and testing set.

# Chapter 3: Evaluation Metrics for supervised learning

## Classification Metrics

* Accuracy
* Precision ( P )
* Recall ( R )
* F1 Score ( F1 )
* Area under the ROC ( Receiver Operating Characteristic ) curve ( AUC )
* Log loss
* Precision at k ( P @ k )
* Average  precision at k ( AP @ k )
* Mean average precision at k ( MAP @ k )

## Regression Metrics

* Mean Absolute Error ( MAE )
* Mean squared error ( MSE )
* Root mean squared error ( RMSE )
* Root mean squared log error ( RMSLE )
* Mean precentage error ( MPE )
* Mean absolute percentage error ( MAPE )
* $R^2$ score

### Notes :

* We should know which metric to use
* It depends on the kind of data and mostly **about the targets**


