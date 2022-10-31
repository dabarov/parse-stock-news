from rest_framework import serializers

from .models import StockNews


class StockNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockNews
        fields = '__all__'
