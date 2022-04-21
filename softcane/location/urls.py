from django.urls import path, include
from .views import (zone_view,zone_create_view,ZoneUpdateView,ZoneDeleteView,
                    sub_location_view,sub_location_create_view,SubLocationUpdateView,SubLocationDeleteView,
                    field_view,field_create_view,FieldUpdateView,FieldDeleteView,
                    branch_view, branch_create_view, BranchUpdateView, BranchDeleteView)

urlpatterns = [
    #Articles url
    path('', zone_view, name="zones"),
    path('zone_create/',zone_create_view, name = 'zone_create'),
    path('<pk>/zone_update/', ZoneUpdateView.as_view(), name = 'zone_update'),
    path('<pk>/zone_delete/',ZoneDeleteView.as_view(), name = 'zone_delete'),
    #Sub-Location urls
    path('sublocation/', sub_location_view, name="sublocation"),
    path('sublocation_create/', sub_location_create_view, name='sublocation_create'),
    path('<pk>/sublocation_update/', SubLocationUpdateView.as_view(), name='sublocation_update'),
    path('<pk>/sublocation_delete/', SubLocationDeleteView.as_view(), name='sublocation_delete'),
    #Fields urls
    path('field/', field_view, name="field"),
    path('field_create/',field_create_view, name = 'field_create'),
    path('<pk>/field_update/', FieldUpdateView.as_view(), name = 'field_update'),
    path('<pk>/field_delete/',FieldDeleteView.as_view(), name = 'field_delete'),
    #Branch urls
    path('branch/', branch_view, name="branch"),
    path('branch_create/',branch_create_view, name = 'branch_create'),
    path('branch/<pk>/branch_update/', BranchUpdateView.as_view(), name = 'branch_update'),
    path('branch/<pk>/branch_delete/',BranchDeleteView.as_view(), name = 'branch_delete'),
]
