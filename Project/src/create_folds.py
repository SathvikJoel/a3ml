import numpy as np
import pandas as pd
from sklearn import model_selection

if __name__ == '__main__':
    df = pd.read_csv('../input/cat-to-dat/train.csv')

    df['Kfold'] = -1

    df.sample(frac = 1).reset_index(drop= True)

    kf = model_selection.KFold(n_splits=5)

    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        df.loc[val_, 'Kfold'] = fold
    
    df.to_csv('../input/cat-to-dat/train_folds.csv', index = False)


