import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#initialization of data ingestion config
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test_csv')
    raw_data_path=os.path.join('artifacts','raw_data')

#create a dataingestion class
class DataIngestion:
    def __init__(self):
        self.dataingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion method starts.')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','UCI_Credit_Card.csv'))
            logging.info('Data read as a pandas dataframe.')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)

            logging.info('Data saving as train and test data separately.')
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data ingestion completed.')

            return(
                self.ingestion_config.train_data_path
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Error occured in Data Ingestion config')


