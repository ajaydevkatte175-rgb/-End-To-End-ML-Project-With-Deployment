import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")          # directory for logs
os.makedirs(logs_dir, exist_ok=True)                 # create logs/ if missing

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)     # full path for the single log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}")
