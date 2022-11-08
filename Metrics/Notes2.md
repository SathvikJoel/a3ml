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


# Classification Metrics

## Basic Definitions:

* **True Positive ( TP )** : The number of positive samples correctly classified as positive
* **True Negative ( TN )** : The number of negative samples correctly classified as negative
* **False Positive ( FP )** : The number of negative samples incorrectly classified as positive, also called Type I error
* **False Negative ( FN )** : The number of positive samples incorrectly classified as negative, also called Type II error

## Confusion Matrix

<p align="center">
![logo](../Images/ConfusionMatrix.png)
</p>


## Accuracy:

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

* Accuracy is the most basic metric
* Only useful when the dataset is balanced

In case the dataset is skewed, we can use the following metrics:

## Precision:

$$Precision = \frac{TP}{TP + FP}$$

$$Recall = \frac{TP}{TP + FN}$$

In other words,

$$Precision = \frac{True~Positives}{Total~Predicted~ Positives}$$

$$Recall = \frac{True~Positives}{Total~Actual~ Positives}$$

Why precison and recall are important?

In unbalanced datasets, one can get high accuracy just by predicting the majority class for all samples. For example, if we have 90% of samples belonging to class 0 and 10% of samples belonging to class 1, then a classifier that predicts class 0 for all samples will get 90% accuracy. However, this classifier will miss all the samples belonging to class 1. So, accuracy is not a good metric in such cases.

Such simple stratagies can't fool precision and recall at the same time

For a good model, both precision and recall must be high.

Combine both of these  topics into a single metric called F1 score

## F1 Score:

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

* F1 score is the harmonic mean of precision and recall

## Threshold for classification

Usually in classification we get a prbability score, we need to convert them to binary values, using threshold. 

* The default threshold is 0.5

But it can be any other value.

## Precision Recall Curve

Draw a graph between precision and recall for different thresholds.

## How to visualize the following topics.

Imagine a confusion matrix, ther columns have the actual values. So number of samples in a column always remains the same. Depending on your decision you can place them in the rows.

threshold basically moves the samples between rows. So, the metrics change. We need to choose the bet metrics, that balances all the metrics. It is dependent on what wee want. 

Sometimes we want less False Positives, sometimes we want less False Negatives. Depending on this, we take the threshold.


## Specificity

$$Specificity = \frac{TN}{TN + FP}$$

* Also called True Negative Rate ( TNR )

## Sensitivity

$$Sensitivity = \frac{TP}{TP + FN}$$

* Also called True Positive Rate ( TPR )

## False Positive Rate

$$FPR = \frac{FP}{FP + TN}$$

## Area under the ROC ( Receiver Operating Characteristic ) curve ( AUC )

ROC is the curve between TPR and FPR.

It will let us determine the best threshold. We should choose the threshold that gives us the best TPR and FPR.
Sometimes we need to deicde the threshold based on the business requirements, as stated eariler.

**Area under the ROC curve is a good metric to compare different models.**

## Notes for AUC

* It varies bwtween 0 and 1
* 0.5 == Random Model
* 1 == Perfect Model, something is wrong with the code
* 0 == Best/ Worst Model depending on the code
* Values closer to 1 are better
* Values between 0.5 and 1 are worse than random, flip the probabilities to change it

## Log loss

For  a single sample, it is

$$LogLoss = -y \times log(p) - (1 - y) \times log(1 - p)$$

* Note : Log loss penalizes when your answers are not confident enough
  
That is if you are 51% sure of the correct answer, other metrics would not penalize you, but log loss will penalize you.

## Extentions For MultiClass Classification

All the above formulas can be extended to multi class classification with a few modifications.

### Macro Versions

Its one vs all approch. We calculate the metrics for each class and then take the average.

### Micro Versions

Calculate class wise TP, TN, FP, FN for all the classes and then calculate the metrics.

### Weighted Versions

Calculate class wise TP, TN, FP, FN for all the classes and then calculate the metrics. But this time, we give more weightage to the classes that have more samples. There are several ways to do this.

## Multi Label Classification

A sample can belong to multiple classes.

### Precision at k ( P @ k )

Consider the top K confident predictions and calculate the number of hots, divided by K.

### Average  precision at k ( AP @ k )

It is the avergae of P@K for K = 1 to K 

### Mean average precision at k ( MAP @ k )

It is the average of AP@K for all the samples.

## Matthews Correlation Coefficient ( MCC )

$$MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}$$

* It can be used for imbalanced datasets
* values closer to 1 are better, values closer to -1 are worse, 0 is random


# Regression Metrics

* Error = Actual - Predicted
* Absolute Error = |Error|
* Squared Error = Error^2
* Squared Log Error = (log(Actual + 1) - log(Predicted + 1))^{2}
* Percentage error = (Actual - Predicted)/Actual * 100
* Absolute Percentage Error = |Percentage Error|


## MEA ( Mean Absolute Error )

Mean of all Absolute Errors

## MSE ( Mean Squared Error )

Mean of all Squared Errors

## RMSE ( Root Mean Squared Error )

Square root of MSE

## Mean Percentage Error ( MPE )

Mean of all Percentage Errors

## Mean Absolute Percentage Error ( MAPE )

Mean of all Absolute Percentage Errors

## $R^2$ score

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

* SS_res = Sum of Squared Residuals ( Error  Squared )
* SS_tot = Total Sum of Squares ( True - Mean of true values )

* It tells us how the regression is performing






