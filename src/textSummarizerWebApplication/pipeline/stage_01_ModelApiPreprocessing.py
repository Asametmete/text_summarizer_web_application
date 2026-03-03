from src.textSummarizerWebApplication.components.ModelApiPreprocessing import ModelApiPreprocessing
from src.textSummarizerWebApplication.config.configuration import ConfigurationManager

class ModelApiPreprocessingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_Api_Processing_Entity = config.get_Model_Api()
        model_Api_Processing = ModelApiPreprocessing(config = model_Api_Processing_Entity)

        model = model_Api_Processing.load_model_from_pretrained()
        tokenizer = model_Api_Processing.load_tokenizer_from_pretrained()
        model_Api_Processing.convert_modelandTokenizer_pkl(model, tokenizer)


