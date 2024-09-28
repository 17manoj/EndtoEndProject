from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd
from mlProject import logger

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status =None
            data = pd.read_csv( self.config.unzip_dir)
            all_data_cols = list(data.columns)
            all_columns = self.config.all_schema.keys()

            for data_col in all_data_cols:
                if data_col not in all_columns:
                    validation_status= False
                    
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'validation_status: {validation_status}')

                else:
                    
                    validation_status= True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'validation_status: {validation_status}')
            return validation_status
        except Exception as e:
            raise e                        

