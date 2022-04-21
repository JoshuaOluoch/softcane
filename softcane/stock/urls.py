from django.urls import path, include
from .views import (stock_category_view, stock_category_create_view, StockCategoryUpdateView, StockCategoryDeleteView,
                    stock_item_view, stock_item_create_view, StockItemUpdateView, StockItemDeleteView,
                    fuel_type_view, fuel_type_create_view, FuelTypeUpdateView, FuelTypeDeleteView,
                    fuel_pump_view, fuel_pump_create_view, FuelPumpUpdateView, FuelPumpDeleteView,
                    tank_view, tank_create_view, TankUpdateView, TankDeleteView,
                    fuel_readings_view,fuel_readings_create_view, FuelReadingsUpdateView, FuelReadingsDeleteView,
                    stock_article_issue_view, stock_article_issue_create_view, StockArticleIssueUpdateView, StockArticleIssueDeleteView,
                    stock_article_adjustment_view, stock_article_adjustment_create_view, StockArticleAdjustmentUpdateView, StockArticleAdjustmentDeleteView)

from .stock_receipt_view import StockArticleReceiptList, StockArticleReceiptItemCreate, StockArticleReceiptItemUpdate, StockArticleReceiptDelete

urlpatterns = [
    #Stock Category url
    path('', stock_category_view, name="stock_categories"),
    path('stock_category_create/',stock_category_create_view, name = 'stock_category_create'),
    path('<pk>/stock_category_update/', StockCategoryUpdateView.as_view(), name = 'stock_category_update'),
    path('<pk>/stock_category_delete/',StockCategoryDeleteView.as_view(), name = 'stock_category_delete'),
    #Stock Item urls
    path('stock_items/', stock_item_view, name="stock_items"),
    path('stock_item_create/', stock_item_create_view, name='stock_item_create'),
    path('stock_items/<pk>/stock_item_update/', StockItemUpdateView.as_view(), name='stock_item_update'),
    path('stock_items/<pk>/stock_item_delete/', StockItemDeleteView.as_view(), name='stock_item_delete'),
    #Fuel Type urls
    path('fuel_type/', fuel_type_view, name="fuel_type"),
    path('fuel_type_create/',fuel_type_create_view, name = 'fuel_type_create'),
    path('fuel_type/<pk>/fuel_type_update/', FuelTypeUpdateView.as_view(), name = 'fuel_type_update'),
    path('fuel_type/<pk>/fuel_type_delete/',FuelTypeDeleteView.as_view(), name = 'fuel_type_delete'),
    #Tank urls
    path('tank/', tank_view, name="tank"),
    path('tank_create/',tank_create_view, name = 'tank_create'),
    path('tank/<pk>/tank_update/', TankUpdateView.as_view(), name = 'tank_update'),
    path('tank/<pk>/tank_delete/',TankDeleteView.as_view(), name = 'tank_delete'),

    #Fuel Pumps urls
    path('fuel_pump/', fuel_pump_view, name="fuel_pump"),
    path('fuel_pump_create/',fuel_pump_create_view, name = 'fuel_pump_create'),
    path('fuel_pump/<pk>/fuel_pump_update/', FuelPumpUpdateView.as_view(), name = 'fuel_pump_update'),
    path('fuel_pump/<pk>/fuel_pump_delete/',FuelPumpDeleteView.as_view(), name = 'fuel_pump_delete'),

    # Fuel Readings urls
    path('fuel_readings/', fuel_readings_view, name="fuel_readings"),
    path('fuel_readings_create/', fuel_readings_create_view, name='fuel_readings_create'),
    path('fuel_readings/<pk>/fuel_readings_update/', FuelReadingsUpdateView.as_view(), name='fuel_readings_update'),
    path('fuel_readings/<pk>/fuel_readings_delete/', FuelReadingsDeleteView.as_view(), name='fuel_readings_delete'),

    # Stock Article Receipt urls
    path('stock_article_receipt/', StockArticleReceiptList.as_view(), name="stock_article_receipt"),
    path('stock_article_receipt/create/', StockArticleReceiptItemCreate.as_view(), name='stock_article_receipt_create'),
    path('stock_article_receipt/<pk>/stock_article_receipt_update/', StockArticleReceiptItemUpdate.as_view(), name='stock_article_receipt_update'),
    path('stock_article_receipt/<pk>/stock_article_receipt_delete/', StockArticleReceiptDelete.as_view(), name='stock_article_receipt_delete'),
    # Stock Article Issue urls
    path('stock_article_issue/', stock_article_issue_view, name="stock_article_issue"),
    path('stock_article_issue_create/', stock_article_issue_create_view, name='stock_article_issue_create'),
    path('stock_article_issue/<pk>/stock_article_issue_update/', StockArticleIssueUpdateView.as_view(), name='stock_article_issue_update'),
    path('stock_article_issue/<pk>/stock_article_issue_delete/', StockArticleIssueDeleteView.as_view(), name='stock_article_issue_delete'),

    # Stock Article Adjustment urls
    path('stock_article_adjustment/', stock_article_adjustment_view, name="stock_article_adjustment"),
    path('stock_article_adjustment_create/', stock_article_adjustment_create_view, name='stock_article_adjustment_create'),
    path('stock_article_adjustment/<pk>/stock_article_adjustment_update/', StockArticleAdjustmentUpdateView.as_view(), name='stock_article_adjustment_update'),
    path('stock_article_adjustment/<pk>/stock_article_adjustment_delete/', StockArticleAdjustmentDeleteView.as_view(), name='stock_article_adjustment_delete'),
]