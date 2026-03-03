from src.textSummarizerWebApplication.components.ModelApiCreating import ModelApiCreating
from src.textSummarizerWebApplication.config.configuration import ConfigurationManager


class ModelApiCreatingPipeline:
    def __init__(self):
        config = ConfigurationManager()
        model_Api_Creating_Entity = config.get_Model_Api()
        # instantiate the component that defines FastAPI app and its endpoints
        self.api_creator = ModelApiCreating(config=model_Api_Creating_Entity)

    def main(self):
        # use the component's create_app() method to load model/tokenizer and
        # return the ready-to-run FastAPI app
        app = self.api_creator.create_app()
        return app