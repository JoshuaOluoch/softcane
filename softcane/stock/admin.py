from django.contrib import admin
from .models import (FuelPump, FuelType, Tank, StockItem, StockCategory, StockArticleReceipt,
                     StockArticleIssue, StockArticleAdjustment, FuelReadings, StockArticleReceiptItem)

admin.site.register(FuelPump)
admin.site.register(FuelType)
admin.site.register(Tank)
admin.site.register(StockItem)
admin.site.register(StockCategory)
admin.site.register(StockArticleReceipt)
admin.site.register(StockArticleIssue)
admin.site.register(StockArticleAdjustment)
admin.site.register(FuelReadings)
admin.site.register(StockArticleReceiptItem)
