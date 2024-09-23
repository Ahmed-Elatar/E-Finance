from import_export import resources 
from .models import *




class TickerResource(resources.ModelResource):
    class Meta:
        model = Ticker

class HistoryResource(resources.ModelResource):
    class Meta:
        model = History