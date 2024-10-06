from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd
from mlProject import logger
from sklearn.model_selection import train_test_split
import os


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config= config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        print(data.columns)
        X_train, X_test, y_train, y_test = train_test_split( data.drop('quality',axis=1), data['quality'], test_size=0.33, random_state=42)
        pd.DataFrame(X_train).to_csv(os.path.join(self.config.root_dir,"X_train.csv"),index=False)
        pd.DataFrame(X_test).to_csv(os.path.join(self.config.root_dir,"X_test.csv"),index=False)
        pd.DataFrame(y_train).to_csv(os.path.join(self.config.root_dir,"y_train.csv"),index=False)
        pd.DataFrame(y_test).to_csv(os.path.join(self.config.root_dir,"y_test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(X_train.shape)
        logger.info(y_train.shape)