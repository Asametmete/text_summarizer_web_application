from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelApiEntity:
    root_dir:Path
    model_pretrained_path:Path
    model_path:Path
    tokenizer_path:Path