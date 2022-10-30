from django.urls import path

from .views import get_stock_news

urlpatterns = [
    path('<str:stock>/', get_stock_news, name="stock_news")
]
