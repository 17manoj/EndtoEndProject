from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
data_ingestion = DataIngestionTrainingPipeline()
data_ingestion.main()
logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\nx======================x')



STAGE_NAME = "Data Validation Stage"
logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
data_validation = DataValidationTrainingPipeline()
data_validation.main()
logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\nx======================x')

STAGE_NAME = "Data Transformation Stage"
logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
data_validation = DataTransformationTrainingPipeline()
data_validation.main()
logger.info(f'>>>>> Stage {STAGE_NAME} completed <<<<<\n\nx======================x')