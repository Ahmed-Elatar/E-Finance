from celery import shared_task
from .models import *
from .serializers import *
from time import sleep
import yfinance as yf



@shared_task
def update_tickers_data():
    tickers =Ticker.objects.all()
    for tk in tickers:
        
        ticker_data = yf.Ticker(tk.symbol)
        info = ticker_data.info
        print(234)
        price = info.get('currentPrice')
        volume = info.get('volume')
        history_data = {
                    'ticker': tk.id,  
                    'price': price,
                    'volume': volume,
                    'date': timezone.now()  # Capture the update time
                }
        serializer = HistorySerializer(data=history_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(f"Error saving history for ticker {tk.symbol}: {serializer.errors}")














    






