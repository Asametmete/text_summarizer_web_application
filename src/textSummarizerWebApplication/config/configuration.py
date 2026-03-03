from src.textSummarizerWebApplication.utils.common import read_Yaml_File, create_folder
from src.textSummarizerWebApplication.constant import CONFIG_FILE_PATH
from src.textSummarizerWebApplication.entity import ModelApiEntity

from pathlib import Path

class ConfigurationManager:
    def __init__(self):
        self.config = read_Yaml_File(CONFIG_FILE_PATH)

    def get_Model_Api(self) -> ModelApiEntity:
        Model_Api_Entity = ModelApiEntity(Path(self.config["ModelIngestion"]["root_dir"]),
                                          Path(self.config["ModelIngestion"]["model_pretrained_path"]),
                                          Path(self.config["ModelIngestion"]["model_path"]),
                                            Path(self.config["ModelIngestion"]["tokenizer_path"]))
        create_folder(Model_Api_Entity.root_dir)
        return Model_Api_Entity