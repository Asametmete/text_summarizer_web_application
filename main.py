from src.textSummarizerWebApplication.logging import logger
from src.textSummarizerWebApplication.pipeline.stage_02_ModelApiCreating import ModelApiCreatingPipeline
import uvicorn

"""
from src.textSummarizerWebApplication.pipeline.stage_01_ModelApiPreprocessing import ModelApiPreprocessingPipeline

STAGE_01 = "Model Api Preprocessing"

try:
    logger.info(f"Stage {STAGE_01} started")
    model_Api = ModelApiPreprocessingPipeline()
    model_Api.main()
    logger.info(f"{STAGE_01} is succesfully done")
except Exception as e:
    logger.exception(e)
    raise e
"""

STAGE_02 = "Model Api Creating"

try:
    logger.info(f"Stage {STAGE_02} started")
    model_Api_Creating = ModelApiCreatingPipeline()
    app = model_Api_Creating.main()
    logger.info(f"{STAGE_02} is succesfully done")
except Exception as e:
    logger.exception(e)
    raise e


if __name__ == "__main__":
    # run with uvicorn for development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)



