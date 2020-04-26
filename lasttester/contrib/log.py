#coding:utf-8
import logging
from colorlog import ColoredFormatter
from colorama import Fore, init
init(autoreset=True)

LOG_FORMAT_CONSOLE = "%(log_color)s%(asctime)s [%(levelname)-5.5s] %(message)s"
LOG_FORMAT_FILE = "%(asctime)s [%(levelname)-5.5s] %(message)s"

formatter_console = ColoredFormatter(
    LOG_FORMAT_CONSOLE,
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

def color_print(msg, color="WHITE"):
    fore_color = getattr(Fore, color.upper())
    print(fore_color + msg)

def getLogger(log_level='debug', log_file=None,**kwargs):
    logger = logging.getLogger(__name__ if not kwargs.get('name') else kwargs.get('name'))
    if not logger.handlers:
        level = getattr(logging, log_level.upper(), None)
        if not level:
            level = logging.DEBUG
        logger.setLevel(level)
        if log_file:
            handler = logging.FileHandler(log_file, encoding='utf-8')
            handler.setLevel(level)
            handler.setFormatter(LOG_FORMAT_FILE)
            logger.addHandler(handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter_console)
        logger.addHandler(console_handler)
    return logger
