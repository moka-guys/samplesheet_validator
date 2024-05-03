""" logger.py

Class used to create Samplesheet Validator logfiles
"""
import sys
from . import config
import logging
import logging.handlers


def set_root_logger():
    """
    Set up root logger and add stream handler - we only want to add stream handler once
    else it will duplicate log messages to the terminal
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(config.LOGGING_FORMATTER))
    stream_handler.name = "stream_handler"
    logger.addHandler(stream_handler)


def shutdown_logs(logger: object) -> None:
    """
    To prevent duplicate filehandlers and system handlers close
    and remove all handlers for a logging object
        :return (None):
    """
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()


class SSLogger:
    """
    Creates a python logging object with a file handler and syslog handler

    Attributes
        timestamp (str):                        Timestamp from config
        logfile_path (str):                     Name of filepath to provide to _file_handler()
        logging_formatter (logging.Formatter):  Specifies the layout of log records in the final output

    Methods
        get_logger()
            Returns a Python logging object
        _get_file_handler()
            Get file handler for the logger
        _get_syslog_handler()
            Get syslog handler for the logger
    """

    def __init__(self, logfile_path: str):
        """
        Constructor for the Logger class
            :param logfile_path (str):      Path to logfile location
        """
        # Timestamp used for naming log files with datetime, format %Y%m%d_%H%M%S
        self.timestamp = config.TIMESTAMP
        self.logfile_path = logfile_path
        self.logging_formatter = logging.Formatter(config.LOGGING_FORMATTER)

    def get_logger(self) -> logging.Logger:
        """
        Returns a Python logging object, and give it a name
            :return logger (object):    Python logging object with custom attributes
        """
        logger = logging.getLogger()
        logger.filepath = self.logfile_path
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self._get_file_handler())
        logger.addHandler(self._get_syslog_handler())
        logger.timestamp = self.timestamp
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

    def _get_syslog_handler(self) -> logging.handlers.SysLogHandler:
        """
        Get syslog handler for the logger, and give it a name
            :return syslog_handler (logging.SysLogHandler): SysLogHandler
        """
        syslog_handler = logging.handlers.SysLogHandler(address="/dev/log")
        syslog_handler.setLevel(logging.DEBUG)
        syslog_handler.setFormatter(self.logging_formatter)
        syslog_handler.name = "syslog_handler"
        return syslog_handler
