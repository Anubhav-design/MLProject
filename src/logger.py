import logging
import os
from datetime import datetime
LOG_FILE =f"{datetime.now().strftime('%Y_%m_%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)
log_file = os.path.join(log_path, LOG_FILE)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
if __name__ == "__main__":
    logging.info("Logging setup complete.")