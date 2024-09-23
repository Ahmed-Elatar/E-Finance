from django.contrib import admin
from django.urls import path 
from .views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi






schema_view = get_schema_view(
    openapi.Info(
        title="E-Finance ",
        default_version='v1',
    ),
)






urlpatterns = [
    

    path('', schema_view.with_ui('swagger'), name='swagger'),

    path('take-symbol/<str:symbol>', TakeSymbol.as_view() ,name='take-symbol'),

    path('recive/', ReceiveTickerData.as_view() ,name='recive'),
    

    path('tickers/', TickersView.as_view() ,name='tickers'),
    path('ticker/<int:pk>', TickerView.as_view() ,name='ticker'),

    path('tickers-history/', TickersHistoryView.as_view() ,name='tickers-history'),
    path('ticker-history/<int:pk>', TickerHistoryView.as_view() ,name='ticker-history'),

    path('test-y/', test_yahoo ,name='test'),








]
