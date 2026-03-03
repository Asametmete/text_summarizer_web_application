from src.textSummarizerWebApplication.entity import ModelApiEntity
from transformers import T5ForConditionalGeneration, T5Tokenizer
import joblib

class ModelApiPreprocessing:
    def __init__(self, config:ModelApiEntity):
        self.config = config

    def load_model_from_pretrained(self):
        model_dir = self.config.model_pretrained_path

        model = T5ForConditionalGeneration.from_pretrained(model_dir)

        return model
    
    def load_tokenizer_from_pretrained(self):
        model_dir = self.config.model_pretrained_path

        tokenizer = T5Tokenizer.from_pretrained(model_dir)

        return tokenizer
    

    def convert_modelandTokenizer_pkl(self, model, tokenizer):
        Modelpkl_save_dir = self.config.model_path
        Tokenizerpkl_save_dir = self.config.tokenizer_path
        joblib.dump(model, Modelpkl_save_dir)
        joblib.dump(tokenizer, Tokenizerpkl_save_dir)
