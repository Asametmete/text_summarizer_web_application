import logging
import sys
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
os.makedirs("logs", exist_ok=True)
log_filepath = "logs/running_logs.log"

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")