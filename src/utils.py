import os 
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise  CustomException(e,sys)  



'''
def evaluate_models(x_train, y_train,x_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
           

          
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report        
    
'''
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import sys
from src.exception import CustomException

def evaluate_models(x_train, y_train, x_test, y_test, models, param):
    try:
        report = {}

        for name, model in models.items():
            para = param[name]  # ✅ Get hyperparameters using model name

            gs = GridSearchCV(model, para, cv=3)  # ✅ GridSearchCV for tuning
            gs.fit(x_train, y_train)

            best_params = gs.best_params_
            model.set_params(**best_params)  # ✅ Unpack best parameters
            model.fit(x_train, y_train)  # ✅ Train model with best params

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[name] = test_model_score  # ✅ Store results

        return report

    except Exception as e:
        raise CustomException(e, sys)
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)