from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


SATEGE_NAME = "Data evaluation stage"

try:
    logger.info(f">>>>>>>stage {SATEGE_NAME} started <<<<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> stage {SATEGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e