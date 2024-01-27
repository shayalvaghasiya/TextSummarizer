from TextSummarizer.pipeline.stage_01_data_ingetion import DataIngestionTrainingPipeline
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
 