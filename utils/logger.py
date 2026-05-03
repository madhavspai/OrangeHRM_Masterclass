import logging
import os


def get_logger(name):
    # 1. Create a 'logs' directory if it doesn't already exist
    os.makedirs("logs", exist_ok=True)

    # 2. Create the logger object
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 3. The Anti-Spam Check: Avoid duplicate log entries
    if not logger.handlers:
        # 4. The File Handler: Tell the logger to write to a specific file
        file_handler = logging.FileHandler("logs/test_execution.log")
        file_handler.setLevel(logging.INFO)

        # 5. The Format: Define exactly how the text should look
        # e.g., 2026-05-03 15:57:00 - LoginPage - INFO - Entered username
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger