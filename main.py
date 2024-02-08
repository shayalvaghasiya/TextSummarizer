from TextSummarizer.pipeline.stage_01_data_ingetion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_data_training import DataTrainingTrainingPipeline
from TextSummarizer.pipeline.stage_05_data_evaluation import DataEvaluationTrainingPipeline

from TextSummarizer.logging import logger

SATEGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
 


SATEGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
 

SATEGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


SATEGE_NAME = "Data training stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    data_training = DataTrainingTrainingPipeline()
    data_training.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


SATEGE_NAME = "Data evaluation stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    data_training = DataEvaluationTrainingPipeline()
    data_training.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e