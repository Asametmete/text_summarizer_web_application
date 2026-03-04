from src.textSummarizerWebApplication.components.ModelApiCreating import ModelApiCreating
from src.textSummarizerWebApplication.config.configuration import ConfigurationManager


class ModelApiCreatingPipeline:
    def __init__(self):
        config = ConfigurationManager()
        model_Api_Creating_Entity = config.get_Model_Api()
        self.api_creator = ModelApiCreating(config=model_Api_Creating_Entity)

    def main(self):
        app = self.api_creator.main()
        return app