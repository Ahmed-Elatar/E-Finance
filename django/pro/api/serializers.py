from rest_framework import serializers
from .models import *



class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['name','symbol','current_price', 'price_change','current_volume','volume_change']
        read_only_fields = ['current_price', 'price_change', 'current_volume', 'volume_change']




class HistorySerializer(serializers.ModelSerializer):

    # ticker = serializers.PrimaryKeyRelatedField(queryset=Ticker.objects.all() )
    ticker = TickerSerializer(read_only=True)
    class Meta:
        model = History
        fields = '__all__'
        read_only_fields = ['data']
        depth =1
