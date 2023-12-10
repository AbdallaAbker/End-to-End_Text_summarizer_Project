import os 
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(filename)s: %(module)s: %(message)s]"
log_dir= "logs"
log_filepath = os.path.join(log_dir, "text_summarier.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format = logging_str,

                    handlers=[
                        logging.FileHandler(log_filepath), #to create a log file
                        logging.StreamHandler(sys.stdout) #to show logs on terminal
                    ]
                )

logger = logging.getLogger("textSummarizerLogger")


