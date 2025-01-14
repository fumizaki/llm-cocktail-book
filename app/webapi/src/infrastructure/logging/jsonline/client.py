import os
from typing import Union
import logging
from logging import Logger, Formatter, StreamHandler
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from zoneinfo import ZoneInfo
import threading

# 環境変数から設定を読む
LOGGING_DIR = os.getenv('LOGGING_DIR', './logs')
ENV = os.getenv('ENV', 'development')

# 環境に応じたログレベル設定
if ENV == 'production':
    LOGGER_LEVEL = logging.INFO
    FILE_HANDLER_LEVEL = logging.INFO
    CONSOLE_HANDLER_LEVEL = logging.WARNING
else:
    LOGGER_LEVEL = logging.DEBUG
    FILE_HANDLER_LEVEL = logging.DEBUG
    CONSOLE_HANDLER_LEVEL = logging.DEBUG

PROPAGATE = False

class JsonLineLoggingClient:
    """
    Logging Policy
    * Critical: ...
    * Error: ...
    * Warning: ...
    * Info: ...
    * Debug: ...
    """
    _lock = threading.Lock()

    @staticmethod
    def ensure_dir(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

    @staticmethod
    def set_handler(logger: Logger, handler: Union[StreamHandler, TimedRotatingFileHandler], level: int) -> Logger:
        handler.setLevel(level)
        handler.setFormatter(
            Formatter(
                '{"asctime": "%(asctime)s", "thread": "%(thread)d", "process": "%(process)d", '
                '"name": "%(name)s", "funcname": "%(funcName)s", "lineno": "%(lineno)s", '
                '"levelname": "%(levelname)s", "message": "%(message)s"}'
            )
        )
        logger.addHandler(handler)
        return logger

    @classmethod
    def get_logger(cls, module: str) -> Logger:
        with cls._lock:
            logger = logging.getLogger(module)
            if not logger.hasHandlers():
                cls.ensure_dir(LOGGING_DIR)
                
                # タイムローテーションハンドラー
                log_file = os.path.join(
                    LOGGING_DIR,
                    datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y%m%d') + '.jsonl'
                )
                file_handler = TimedRotatingFileHandler(
                    log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8'
                )
                cls.set_handler(logger, file_handler, FILE_HANDLER_LEVEL)
                
                # コンソールハンドラー
                console_handler = StreamHandler()
                cls.set_handler(logger, console_handler, CONSOLE_HANDLER_LEVEL)
                
                logger.setLevel(LOGGER_LEVEL)
                logger.propagate = PROPAGATE
            return logger