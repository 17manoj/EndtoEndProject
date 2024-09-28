from mlProject.config.configuration import configurationManager
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()



if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\nx======================x')

    except Exception as e:
        logger.exception(e)
        raise e