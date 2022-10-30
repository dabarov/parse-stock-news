from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StockNews
from .serializers import StockNewsSerializer


@api_view()
def get_stock_news(request, stock):
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    stock_news = StockNews.objects.filter(related=stock)
    if date_from:
        stock_news = stock_news.filter(published_time__gte=date_from)
    if date_to:
        stock_news = stock_news.filter(published_time__lte=date_to)
    serializer = StockNewsSerializer(stock_news, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
