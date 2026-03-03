import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
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