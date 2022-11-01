from django.urls import path

from .views import get_stock_news, get_daily_summary

urlpatterns = [
    path('stock/<str:stock>/', get_stock_news, name="stock_news"),
    path('daily-summary/', get_daily_summary, name="daily-summary"),
]
