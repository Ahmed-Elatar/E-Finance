from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resource import * 
# Register your models here.




@admin.register(Ticker)
class TickerAdmin(ImportExportModelAdmin):
    resource_class = TickerResource
    list_display =['name','symbol','current_price', 'price_change','current_volume','volume_change','last_update']
    readonly_fields = [field.name for field in Ticker._meta.fields]     
    ordering = ['name'] 

    def has_add_permission(self, request):
        return False    


@admin.register(History)
class HistoryAdmin(ImportExportModelAdmin):
    resource_class = HistoryResource
    list_display =['ticker','date','price', 'volume']
    readonly_fields = [field.name for field in History._meta.fields]
    ordering = ['ticker','-date'] 

    def has_add_permission(self, request):
        return False 