from celery import shared_task
from .models import *
from .serializers import *
from time import sleep
import yfinance as yf





"""
update_tickers_data Function :~

It's a celery task used to get updated price and volume data from yfinance to the tickers
and save it in History model .
"""
@shared_task
def update_tickers_data():
    tickers =Ticker.objects.all()
    for tk in tickers:
        
        ticker_data = yf.Ticker(tk.symbol)
        info = ticker_data.info
        price = info.get('currentPrice')
        volume = info.get('volume')
        history_data = {
                    'ticker': tk.id,  
                    'price': price,
                    'volume': volume,
                    'date': timezone.now()  
                }
        serializer = HistorySerializer(data=history_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(f"Error saving history for ticker {tk.symbol}: {serializer.errors}")














    






