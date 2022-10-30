import os

import finnhub
from celery import shared_task

finnhub_client = finnhub.Client(api_key=os.getenv("FIN_HUB_KEY"))


@shared_task()
def fetch_ticker_news():
    return finnhub_client.company_news('AAPL', _from="2022-06-01", to="2022-06-10")
