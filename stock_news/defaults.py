import os
from datetime import datetime

import finnhub

TICKERS_TO_PARSE = ["TSLA", "FB", "AMZN", "TWTR", "NFLX"]
TODAY = datetime.today().strftime('%Y-%m-%d')
FINNHUB_CLIENT = finnhub.Client(api_key=os.getenv("FIN_HUB_KEY"))
