from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stock_news.defaults import TICKERS_TO_PARSE, TODAY
from stock_news.models import StockNews
from stock_news.serializers import StockNewsSerializer


@api_view()
def get_stock_news(request, stock):
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    stock_news = StockNews.objects.filter(related=stock)
    if date_from:
        stock_news = stock_news.filter(published_time__date__gte=date_from)
    if date_to:
        stock_news = stock_news.filter(published_time__date__lte=date_to)
    serializer = StockNewsSerializer(stock_news, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view()
def get_daily_summary(request):
    total_daily_summary = []
    today_news = StockNews.objects.filter(published_time__date=TODAY)
    for ticker in TICKERS_TO_PARSE:
        ticker_news = today_news.filter(related=ticker)[:5]
        ticker_news_headlines = "\n".join([news.headline for news in ticker_news])
        total_daily_summary.append({
            "ticker": ticker,
            "news": ticker_news_headlines
        })
    return Response(data=total_daily_summary, status=status.HTTP_200_OK)
