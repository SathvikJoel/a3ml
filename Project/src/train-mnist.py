import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import tree
import joblib
import argparse

import model_dispatcher

import config

def run(fold, model):
    # read the training data with folds
    df = pd.read_csv(config.TRAINING_FILE)

    #training data is where KFold is not equal to fold
    df_train = df[df.Kfold != fold].reset_index(drop = True)

    #validation data is where KFold is equal to provided fold
    df_valid = df[df.Kfold == fold].reset_index(drop = True)

    x_train = df_train.drop('label', axis = 1).values
    y_train = df_train.label.values

    x_valid = df_valid.drop('label', axis = 1).values
    y_valid = df_valid.label.values

    clf = model_dispatcher.models[model]

    clf.fit(x_train, y_train)

    preds = clf.predict(x_valid)

    accuracy = metrics.accuracy_score(y_valid, preds)
    print(f"Fold = {fold}, Accuracy = {accuracy}")

    joblib.dump(clf, f"{config.MODEL_OUTPUT} + dt_{fold}.bin")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--fold", type = int)
    parser.add_argument("--model", type = str)
    args = parser.parse_args()

    run(fold = args.fold, model = args.model)