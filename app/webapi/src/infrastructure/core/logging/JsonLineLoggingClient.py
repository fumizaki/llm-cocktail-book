import os
from typing import Union
from logging import Logger, getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO
from datetime import datetime, timedelta, timezone


LOGGING_DIR = "/log"
# 開発環境のみDEBUGを指定する(それ以外はINFO)
LOGGER_LEVEL = DEBUG
# 開発環境のみDEBUGを指定する(それ以外はINFO)
FILE_HANDLER_LEVEL = DEBUG
# 開発環境のみDEBUGを指定する(それ以外はINFO)
CONSOLE_HANDLER_LEVEL = DEBUG
PROPAGATE = False



class JsonLineLoggingClient:
    """
    Logging Policy
    * Cretical: システム全体に影響を与える深刻な問題を記録する

        アプリケーションのクラッシュ
    
        データベース接続の喪失
        
        セキュリティ侵害

    * Error: 特定の操作や機能の失敗を記録する

        ユーザーのアクションによるエラー（不正な入力など）
    
        外部APIとの通信エラー
    
        予期せぬ例外
    
    * Warning: 現時点では問題ないが、将来的に問題になる可能性がある事象を記録する
    
        デプリケーションされた機能の使用
        
        リソース使用率が高くなっている状況
        
        設定の不整合

    * Info: ステムの正常な動作を示す重要なイベントを記録する
        
        アプリケーションの起動と停止
        
        ユーザーのログイン/ログアウト
        
        重要なビジネスプロセスの完了
    
    * Debug: 開発時に必要なデータを記録する
    """


    loggers = {}

    
    @staticmethod
    def is_exist_dir(dir_path: str) -> bool:
        return os.path.exists(dir_path)
    
    @staticmethod
    def set_handler(logger: Logger, handler: Union[StreamHandler, FileHandler], level: str):
        handler.setLevel(level)
        handler.setFormatter(
            Formatter(
                '{"asctime": "%(asctime)s", "thread": "%(thread)d", "process": "%(process)d", "name": "%(name)s", "funcname": "%(funcName)s", "lineno: "%(lineno)s", "levelname": "%(levelname)s", "messages": "%(message)s"}'
                )
            )
        logger.addHandler(handler)
        return logger
    
    @classmethod
    def get_logger(cls, module) -> Logger:
        
        if not cls.is_exist_dir(LOGGING_DIR):
            os.mkdir(LOGGING_DIR)
        
        if cls.loggers.get(module):
            return cls.loggers.get(module)
        
        log_file = LOGGING_DIR + datetime.now(timezone(timedelta(hours=+9), 'Asia/Tokyo')).date().strftime('%Y%m%d') + '.jsonl'
        
        logger = getLogger(module)
        logger = cls.set_handler(logger, StreamHandler(), CONSOLE_HANDLER_LEVEL)
        logger = cls.set_handler(logger, FileHandler(log_file), FILE_HANDLER_LEVEL)
        logger.setLevel(LOGGER_LEVEL) # ロガー自体が処理するログメッセージの最小レベルを設定(DEBUG < INFO < WARNING < ERROR < CRITICAL)
        logger.propagate = PROPAGATE # ログメッセージの伝播（propagation）を制御(Trueの場合：親ロガーにも伝播され、同じメッセージが複数回ログに記録される可能性がある)
        
        cls.loggers[module] = logger
        return logger