import logging

# hoge.fuga.piyoという名前を設定する
logger = logging.getLogger("hoge.fuga.piyo")
# INFOレベル以上のログを出力する
logger.setLevel(logging.INFO)
# ファイルを出力先とするハンドラーを作成
handler = logging.FileHandler("test.log")
# INFOレベル以上のログを出力する
handler.setLevel(logging.INFO)
# ロガー名がhoge.fugaにマッチする場合のみ出力する
logging_filter = logging.Filter("hoge.fuga")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# ハンドラーにフォーマッターを設定する
handler.setFormatter(formatter)
# ハンドラーにフィルターを設定する
handler.addFilter(logging_filter)
# ロガーにハンドラーを設定する
logger.addHandler(handler)
# ロガーにフィルターを設定する
logger.addFilter(logging_filter)
logger.debug("debug message")
logger.info("info message")
