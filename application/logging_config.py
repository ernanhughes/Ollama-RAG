import logging

def configure_logging(log_file='app.log', level=logging.DEBUG):
    """Configures logging for the Flask application.

    Args:
        log_file (str, optional): Path to the log file. Defaults to 'app.log'.
        level (int, optional): Logging level. Defaults to logging.DEBUG.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)


    # add to file
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)
    logger.addHandler(fh)

    return logger