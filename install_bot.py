#!/usr/bin/env python3
  import os

  files = {}

  files["config.py"] = '''SYMBOL = "GC=F"
  TRADING_SYMBOL = "XAUUSD"
  CONTRACT_SIZE = 1
  CONFIDENCE_THRESHOLD_LONG = 80.0
  CONFIDENCE_THRESHOLD_SHORT = 80.0
  CONFIDENCE_EXIT = 20.0
  MAX_OPEN_POSITIONS = 1
  POSITION_SIZE = 1
  TIMEFRAMES = ["1m", "5m", "1h", "4h", "1d"]
  TIMEFRAME_WEIGHTS = {"1m": 0.8, "5m": 1.0, "1h": 1.2, "4h": 1.5, "1d":
  2.0}
  INDICATOR_CATEGORY_WEIGHTS = {"trend": 1.5, "momentum": 1.2, "volatility":
   1.0, "volume": 1.0, "other": 0.8}
  EMA_FAST, EMA_MID, EMA_SLOW, EMA_TREND = 9, 21, 50, 200
  MACD_FAST, MACD_SLOW, MACD_SIGNAL = 12, 26, 9
  RSI_PERIOD, RSI_OVERSOLD, RSI_OVERBOUGHT = 14, 30, 70
  STOCH_K, STOCH_D, STOCH_SMOOTH = 14, 3, 3
  CCI_PERIOD, WILLIAMS_PERIOD, ROC_PERIOD = 20, 14, 12
  BB_PERIOD, BB_STD = 20, 2
  ATR_PERIOD, STDDEV_PERIOD, OBV_PERIOD = 14, 20, 20
  PIVOT_PERIOD = "D"
  NEWS_FETCH_INTERVAL_MINUTES = 5
  SENTIMENT_WEIGHT = 0.15
  MAX_NEWS_ARTICLES = 10
  NEWS_KEYWORDS = ["gold", "XAU", "gold price", "gold trading", "gold
  market", "gold futures"]
  TRADOVATE_BASE_URL = "https://api.tradovate.com/v1"
  TRADOVATE_USER = "TotallyNotYa"
  TRADOVATE_PASSWORD = "Lolzies@25"
  TRADOVATE_DEVICE_ID = "gold-bot-001"
  PAPER_TRADING = True
  WEBHOOK_HOST = "0.0.0.0"
  WEBHOOK_PORT = 5000
  WEBHOOK_PATH = "/webhook"
  WEBHOOK_SECRET = "goldbot2026"
  YFINANCE_SYMBOL = "GC=F"
  GDELT_BASE_URL = "https://api.gdeltproject.org/api/v2/doc/doc"
  LOG_LEVEL = "INFO"
  LOG_FILE = "trading_bot.log"
  TRADE_LOG_FILE = "trade_log.csv"
  '''

  files["utils.py"] = '''import os, sys, logging, logging.handlers
  from datetime import datetime
  from pathlib import Path
  LOG_FILE = "trading_bot.log"
  TRADE_LOG_FILE = "trade_log.csv"
  def setup_logging():
      logger = logging.getLogger("gold_trader")
      logger.setLevel(logging.INFO)
      if logger.handlers: return logger
      fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S")
      fh = logging.handlers.RotatingFileHandler(Path(__file__).parent /
  LOG_FILE, maxBytes=10_000_000, backupCount=5)
      fh.setLevel(logging.DEBUG); fh.setFormatter(fmt);
  logger.addHandler(fh)
      ch = logging.StreamHandler(sys.stdout); ch.setLevel(logging.INFO);
  ch.setFormatter(fmt); logger.addHandler(ch)
      return logger
  logger = setup_logging()
  def log_trade(action, symbol, quantity, price, confidence, reason=""):
      import csv
      timestamp = datetime.utcnow().isoformat()
      logger.info(f"TRADE: {action} {quantity} {symbol} @ {price:.2f} |
  Confidence: {confidence:.1f}% | Reason: {reason}")
      f = Path(__file__).parent / TRADE_LOG_FILE
      with open(f, "a", newline="") as csvfile:
          w = csv.writer(csvfile)
          if not f.exists(): w.writerow(["timestamp","action","symbol","quan
  tity","price","confidence","reason"])
          w.writerow([timestamp, action, symbol, quantity, price,
  confidence, reason])
  def format_confidence_report(scores):
      lines = ["="*50, "CONFIDENCE REPORT", "="*50, f"Overall:
  {scores.get('overall',0):.1f}% | Signal:
  {scores.get('signal','NEUTRAL')}", f"Sentiment:
  {scores.get('sentiment',0):.1f}%"]
      for cat, score in scores.get("by_category",{}).items():
  lines.append(f"  {cat.upper()}: {score:.1f}%")
      return "\\n".join(lines)
  '''

  os.makedirs("indicators", exist_ok=True)
  for path, content in files.items():
      with open(path, "w") as f: f.write(content)
      print(f"Created {path}")
  print("BASE FILES WRITTEN")
