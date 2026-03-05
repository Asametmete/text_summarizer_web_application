from src.textSummarizerWebApplication.components.ModelApiCreating import ModelApiCreating
from src.textSummarizerWebApplication.config.configuration import ConfigurationManager


class ModelApiCreatingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_Api_Creating_Entity = config.get_Model_Api()
        model_Api_Creating = ModelApiCreating(config=model_Api_Creating_Entity)
        model=model_Api_Creating.get_ModelPkl()
        tokenizer=model_Api_Creating.get_TokenizerPkl()
        model_Api_Creating.summarize_text(model,tokenizer)