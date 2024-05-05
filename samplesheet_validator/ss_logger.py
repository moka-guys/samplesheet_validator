""" logger.py

Class used to create Samplesheet Validator logfiles
"""
import sys
from . import config
import logging
import logging.handlers


def set_root_logger(no_stream_handler: bool):
    """
    Set up root logger and add stream handler and syslog handler - we only want to add these once
    else it will duplicate log messages to the terminal. All loggers named with the same stem
    as the root logger will use these same syslog handler and stream handler
        :param no_stream_handler (bool):    True if no stream handler specified as command line input
    """
    formatter = logging.Formatter(config.LOGGING_FORMATTER)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    syslog_handler = logging.handlers.SysLogHandler(address="/dev/log")
    syslog_handler.setFormatter(formatter)
    syslog_handler.name = "syslog_handler"
    logger.addHandler(syslog_handler)
    if not no_stream_handler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        stream_handler.name = "stream_handler"
        logger.addHandler(stream_handler)
    return logger



class SSLogger:
    """
    Creates a python logging object with a file handler and syslog handler

    Attributes
        logfile_path (str):                     Name of filepath to provide to _file_handler()
        runfolder_name (str):                   Runfolder name
        logging_formatter (logging.Formatter):  Specifies the layout of log records in the final output

    Methods
        get_logger(logger_name)
            Returns a Python logging object
        _get_file_handler()
            Get file handler for the logger
        _get_syslog_handler()
            Get syslog handler for the logger
    """

    def __init__(self, logfile_path: str, runfolder_name: str):
        """
        Constructor for the Logger class
            :param logfile_path (str):      Path to logfile location
            :param runfolder_name (str):    Runfolder name
        """
        # Timestamp used for naming log files with datetime, format %Y%m%d_%H%M%S
        self.logfile_path = logfile_path
        self.runfolder_name = runfolder_name
        self.logging_formatter = logging.Formatter(config.LOGGING_FORMATTER)

    def get_logger(self, logger_name: str) -> logging.Logger:
        """
        Returns a Python logging object, and give it a name
            :param logger_name (str):   Logger name string
            :return logger (object):    Python logging object with custom attributes
        """
        logger = logging.getLogger(f"{logger_name}.{self.runfolder_name}")
        logger.filepath = self.logfile_path
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self._get_file_handler())
        logger.log_msgs = config.LOG_MSGS
        return logger

    def _get_file_handler(self) -> logging.FileHandler:
        """
        Get file handler for the logger, and give it a name
            :return file_handler (logging.FileHandler): FileHandler
        """
        file_handler = logging.FileHandler(self.logfile_path, mode="a", delay=True)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.logging_formatter)
        file_handler.name = "file_handler"
        return file_handler
