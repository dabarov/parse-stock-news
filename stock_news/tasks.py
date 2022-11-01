import os
from datetime import datetime

import finnhub
import requests
from celery import shared_task
from django.utils.timezone import make_aware
from rest_framework import status

from stock_news.models import StockNews

TICKERS_TO_PARSE = ["TSLA", "FB", "AMZN", "TWTR", "NFLX"]
TODAY = datetime.today().strftime('%Y-%m-%d')
finnhub_client = finnhub.Client(api_key=os.getenv("FIN_HUB_KEY"))


@shared_task()
def fetch_tickers_news():
    for ticker in TICKERS_TO_PARSE:
        fetch_ticker_news(ticker)


def fetch_ticker_news(ticker):
    news_list = finnhub_client.company_news(ticker, _from=TODAY, to=TODAY)
    for news in news_list:
        pk = news.pop("id")
        published_time_unix_format = news.pop("datetime")
        published_time = make_aware(datetime.fromtimestamp(published_time_unix_format))
        news["published_time"] = published_time
        StockNews.objects.update_or_create(id=pk, defaults=news)
    if status.is_success(email_newsletter(news_list, ticker)):
        return "SUCCESS"
    else:
        return "FAILURE"


def email_newsletter(news_list, ticker):
    news_headlines = "\n".join([news.get("headline") for news in news_list])
    body = {
        "ticker": ticker,
        "news": news_headlines
    }
    response = requests.post(url="http://host.docker.internal:8002/notifications/email-fetched-news/", json=body)
    return response.status_code
