from src.textSummarizerWebApplication.pipeline.stage_01_ModelApiPreprocessing import ModelApiPreprocessingPipeline
from src.textSummarizerWebApplication.logging import logger


STAGE_01 = "Model Api Preprocessing"

try:
    logger.info(f"Stage {STAGE_01} started")
    model_Api = ModelApiPreprocessingPipeline()
    model_Api.main()
    logger.info(f"{STAGE_01} is succesfully done")
except Exception as e:
    logger.exception(e)
    raise e