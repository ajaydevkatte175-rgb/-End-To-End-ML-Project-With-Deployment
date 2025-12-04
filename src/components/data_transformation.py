import sys
import os
from dataclasses import dataclass
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def initiate_data_transformation(self, train_path, test_path):
        logging.info("Entered Data Transformation")

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data")

            # just dummy transformation for now
            return train_df.values, test_df.values, None

        except Exception as e:
            raise CustomException(e, sys)
