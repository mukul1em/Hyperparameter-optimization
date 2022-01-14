import pandas as pd
import numpy as np
from sklearn import ensemble

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import model_selection





if __name__ == '__main__':
    df = pd.read_csv('input/train.csv')
    X  = df.drop('price_range', axis=1).values
    y  = df.price_range.values

    classifier = ensemble.RandomForestClassifier(n_jobs=-1)
    #parameter grid is dictionary which contains the paramteres which are supposed to be optimized
    param_grid = {
        "n_estimators": [100,200,300,400],
        "max_depth" : [1,3,5,7],
        "criterion" :["gini","entropy"]
    }

    model = model_selection.GridSearchCV(
        estimator=classifier,
        param_grid=param_grid,
        scoring="accuracy",
        verbose=10,
        n_jobs=-1,
        cv=5
    )

    model.fit(X,y)

    print("best score: ",model.best_score_)
    print("best parameters: ",model.best_estimator_.get_params())


#Note:  scoring function can be changed based on the problem statement. make_score from sklearn can be used to build custom scoring modek