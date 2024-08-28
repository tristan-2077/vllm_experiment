import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger with file handling"""
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    file_handler = RotatingFileHandler(os.path.join(log_dir, log_file), maxBytes=10*1024*1024, backupCount=5)
    console_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    console_handler.setFormatter(console_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

my_logger = setup_logger('my_logger', 'debug.log')


# Example usage
if __name__ == "__main__":
    # Set up loggers
    logger1 = setup_logger('logger1', 'logger1.log')
    logger2 = setup_logger('logger2', 'logger2.log')

    # Use loggers
    logger1.info('This is a log message from logger1')
    logger2.warning('This is a warning message from logger2')