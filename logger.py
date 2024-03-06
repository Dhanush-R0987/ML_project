import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strtime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)