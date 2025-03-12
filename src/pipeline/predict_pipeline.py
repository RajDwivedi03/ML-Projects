from src.exception import CustomException
import sys
import numpy as np
import pandas as pd
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        self.model_path = 'artifacts/model.pkl'
        self.preprocessor_path = 'artifacts/preprocessor.pkl'
    
    def predict(self, features):
        try:
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)
            data_scaled = preprocessor.transform(features)
            return model.predict(data_scaled)
        except Exception as e:
            raise CustomException(e, sys)

# Custom Data Class
class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education,
                 lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        return pd.DataFrame({
            "gender": [self.gender],
            "race/ethnicity": [self.race_ethnicity],
            "parental level of education": [self.parental_level_of_education],
            "lunch": [self.lunch],
            "test preparation course": [self.test_preparation_course],
            "reading score": [self.reading_score],
            "writing score": [self.writing_score]
        })