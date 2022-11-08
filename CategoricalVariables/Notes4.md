# Categorical Variables

* Nominal - No order
* Ordinal - Order associated with them
* Cyclic - Order associated with them, but the order is circular
* Binary - Only two values

## Methods of Encoding

### Label Encoding :

Assign a number to each category

* Can be done with `LabelEncoder` from `sklearn.preprocessing`

* LabelEncoder doesnt handle NaN values, this is really important

* After Label encoding we can directly use this in many tree based models but not in Linear Models as they expect data to be normalized


### Binary Representation :

Convert the categories into binary values using the numerical mapping

### One Hot Encoding:

Obvious


#### Memory Usage:

One hot encoding occupies less memeory compared to Binary representation when stored in sparse representation

```python
from scipy import sparse

sparse_example = sparse.csr_matrix(example)
```

### Converting Categorical to Numerical

Replace the categories with the count of the categories in that feature

* Tip : Can combine two rows and then apply this method

### Categorical to More Categorical

Combine two or more categorical columns to form a new categorical column

* Tip : NaNs will be converted to strings but thats not an issue

## Handling Missing Values

1. Drop the rows with missing values ( not preferred )

2. Preferred : Treat NaN as a new texhnique ( use  `fillna`)

## Handling rare categories

If there are not NaN values and the model is deployed and a new 
category in a feature arises then the pipeline fails, if this is expected then we have to deal with them

1. Predict the category: Create a model to predict the cateogry ( in this case the catoegory will be replaced with one of the known categories )

2. In case of fixed test set: Add the testset to the train set and do the modelling of features. ( clearly this is illegal so in this case make sure to create the folds such that the validation set has categories unseen in the training set )

* the above only works when there is a test set already, in live it might not work.

3. For live settings : Create a new category ( use the NONE category, if needed ) and any new category will be converted to this category

4. A slight modificatio of the above is to convert all the cateogries that appear less to a RARE catoegory. So now missing values are NONE and new unseen categories are RARE


### Target Encoding

Replace the categories with mean of the target.

* This needs to be done in a cross validated format. That is create a dataframe in which the encoding of each fold is derived from the rest of the reamining folds.

### Entity Embeddings

Need to think abt this !

# Feature Engennering

* Depends highly on domain knowlwdge

* Feature engeneering is about creatiing new features from the data and also different types of normalization and transformation

## Date and Time

We can create features like 

- year
- Week of the year
- Month
- Day of the week
- Weekend
- Hour

## Aggregated Features

Features that are obtained by aggregating on one of the columns. 

Eg: If there is a coustomer ID column and coustomers are getting repeated, then aggregate on that column and find features based on the rest of the features

Use `group_by` and `agg` to do that.

You can group on categorical features and calculate various statastics on numerical columns

- Mean
- Max
- Min
- Unique
- Skew
- Kurtosis
- Kstat
- Percentile
- Quantile
- Peak to peak

There is a python library called `tsfresh` that helps when dealing with time series data


## Polynomial Features

Create polynomial features from numeraical columns

Use `PolynomilFeatures` from `skelarn.preprocessing`

## Binning 

To create categorical feaures from numerical ones

Use `cut` function from pandas

## Log transformation

Apply `log(1+x)` to reduce the variance

* Sometimes exponential is needed

## Handling missing values

* replace with mean / median
* Replace with some default value corresponing to that column
* use `KNN Imputer` 

* Use a regression model to predict the missing values

* Note: Imputing values for tree-based models is unnecessary as they can handle it themselves

# Feature Selection

## Low variance

Remove features with low variance.

Note : Variance also depends on the scaling

```Python
from sklearn.feature_selection import VarianceThreshold
```

## High Correlation

Use pearson correlation to calculate correlation between different numerical features

```Python
df.corr()
```

## Univariate Feature Selection

Scoring of each feature against a given target 

* Mutual Information, ANOVA F-test, chi2

In sklearn use `SelectKBest` or `SelectPercentile`

`from sklearn.feature_selection import` 

For Classification

* `chi2`
* `f_classif`
* `mutual_info_classif`

For Regression

* `f_regression`
* `mutual_info_regression`

Univaraite Feature selection might not always perform the best

## Feature selection using a ML Algorithm

### Greedy Feature Selection

Steps:
1. Select a model
2. Select a loss/scoring function
3. Iteratively evaluate each feature and add it to list of good features if it improves the score

* Computationally costly, might overfit if not properly used

### Recursive Feature Elmination

Keep removing one features that adds the **least value**

Deciding least value:

* For SVMs and Logistic regression, we get a coefficient that decides the importance of the features

* For tree based models, we get feature importance.

`from sklearn.feature_selection import RFE`

### Direct method

Fit the model and use the feature coefficients or feature importance ( setting a threshld ) to select the features

`from sklearn.feature_selection import SelectFromModel`, specify the number of features and the threshold on the selection

* This could also be done using models that use L1 penalization. Features with non zero coefficients are to be selected since most features will be zero. ( Eg: lasso regression )


