"""
Logging Utilities

Centralized logging configuration and utilities.
"""

import logging
import sys
from pathlib import Path


def setup_logging(level: str = "INFO", log_file: str = None):
    """
    Set up logging configuration.
    
    Args:
        level (str): Logging level
        log_file (str): Optional log file path
    """
    log_level = getattr(logging, level.upper())
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if log_file:
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=log_level,
        handlers=handlers,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def get_logger(name: str):
    """
    Get a logger instance.
    
    Args:
        name (str): Logger name
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)