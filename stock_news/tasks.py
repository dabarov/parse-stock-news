from datetime import datetime

import requests
from celery import shared_task
from django.utils.timezone import make_aware

from stock_news.defaults import TICKERS_TO_PARSE, TODAY, FINNHUB_CLIENT
from stock_news.models import StockNews


@shared_task()
def fetch_tickers_news():
    for ticker in TICKERS_TO_PARSE:
        fetch_ticker_news(ticker)


def fetch_ticker_news(ticker):
    news_list = FINNHUB_CLIENT.company_news(ticker, _from=TODAY, to=TODAY)
    for news in news_list:
        pk = news.pop("id")
        published_time_unix_format = news.pop("datetime")
        published_time = make_aware(datetime.fromtimestamp(published_time_unix_format))
        news["published_time"] = published_time
        StockNews.objects.update_or_create(id=pk, defaults=news)
    if email_newsletter(news_list, ticker):
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
    return response.ok
