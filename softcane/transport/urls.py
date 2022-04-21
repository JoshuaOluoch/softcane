from django.urls import path, include
from .views import (transport_info_view, transport_info_create_view, TransportInfoUpdateView, TransportInfoDeleteView,
                    trip_view, trip_create_view, TripUpdateView, TripDeleteView,
                    fuel_consumption_view, fuel_consumption_create_view, FuelConsumptionUpdateView, FuelConsumptionDeleteView,
                    towing_view, towing_create_view, TowingUpdateView, TowingDeleteView,
                    packed_cane_view, packed_cane_create_view, PackedCaneUpdateView, PackedCaneDeleteView,
                    loaders_entry_view,loaders_entry_create_view, LoadersDailyEntryUpdateView, LoadersDailyEntryDeleteView,
                    pickup_canter_control_view, pickup_canter_control_create_view, PickupsAndCantersControlUpdateView, PickupsAndCantersControlDeleteView,
                    ticket_reconciliation_view, ticket_reconciliation_create_view, TicketReconciliationUpdateView, TicketReconciliationDeleteView,
                    trailer_attachment_view, trailer_attachment_create_view, TrailerAttachmentUpdateView, TrailerAttachmentDeleteView,
                    insurance_validity_view, insurance_risk_create_view, insurance_company_create_view, insurance_validity_create_view,
                    InsuranceRiskUpdateView, InsuranceRiskDeleteView, InsuranceCompanyUpdateView, InsuranceCompanyDeleteView, InsuranceValidityUpdateView, InsuranceValidityDeleteView,
                    driving_licence_validity_view, driving_licence_validity_create_view, DrivingLicenceValidityUpdateView, DrivingLicenceValidityDeleteView)


urlpatterns = [
    #Transport Information url
    path('', transport_info_view, name="transport_info"),
    path('transport_info_create/',transport_info_create_view, name = 'transport_info_create'),
    path('<pk>/transport_info_update/', TransportInfoUpdateView.as_view(), name = 'transport_info_update'),
    path('<pk>/transport_info_delete/',TransportInfoDeleteView.as_view(), name = 'transport_info_delete'),
    #Trips details url
    path('trip/', trip_view, name="trip"),
    path('trip_create/',trip_create_view, name = 'trip_create'),
    path('trip/<pk>/trip_update/', TripUpdateView.as_view(), name = 'trip_update'),
    path('trip/<pk>/trip_delete/',TripDeleteView.as_view(), name = 'trip_delete'),
    #Fuel Consumption url
    path('fuel_consumption/', fuel_consumption_view, name="fuel_consumption"),
    path('fuel_consumption_create/',fuel_consumption_create_view, name = 'fuel_consumption_create'),
    path('fuel_consumption/<pk>/fuel_consumption_update/', FuelConsumptionUpdateView.as_view(), name = 'fuel_consumption_update'),
    path('fuel_consumption/<pk>/fuel_consumption_delete/',FuelConsumptionDeleteView.as_view(), name = 'fuel_consumption_delete'),
    #Towing url
    path('towing/', towing_view, name="towing"),
    path('towing_create/',towing_create_view, name = 'towing_create'),
    path('towing/<pk>/towing_update/', TowingUpdateView.as_view(), name = 'towing_update'),
    path('towing/<pk>/towing_delete/',TowingDeleteView.as_view(), name = 'towing_delete'),
    #Packed Cane url
    path('packed_cane/', packed_cane_view, name="packed_cane"),
    path('packed_cane_create/',packed_cane_create_view, name = 'packed_cane_create'),
    path('packed_cane/<pk>/packed_cane_update/', PackedCaneUpdateView.as_view(), name = 'packed_cane_update'),
    path('packed_cane/<pk>/packed_cane_delete/',PackedCaneDeleteView.as_view(), name = 'packed_cane_delete'),
    #Loaders Entry url
    path('loaders_entry/', loaders_entry_view, name="loaders_entry"),
    path('loaders_entry_create/',loaders_entry_create_view, name = 'loaders_entry_create'),
    path('loaders_entry/<pk>/loaders_entry_update/', LoadersDailyEntryUpdateView.as_view(), name = 'loaders_entry_update'),
    path('loaders_entry/<pk>/loaders_entry_delete/', LoadersDailyEntryDeleteView.as_view(), name = 'loaders_entry_delete'),
    #Pickups and Canters Control url
    path('pickup_canter_control/', pickup_canter_control_view, name="pickup_canter_control"),
    path('pickup_canter_control_create/',pickup_canter_control_create_view, name = 'pickup_canter_control_create'),
    path('pickup_canter_control/<pk>/pickup_canter_control_update/', PickupsAndCantersControlUpdateView.as_view(), name = 'pickup_canter_control_update'),
    path('pickup_canter_control/<pk>/pickup_canter_control_delete/',PickupsAndCantersControlDeleteView.as_view(), name = 'pickup_canter_control_delete'),
    #Ticket Reconciliation url
    path('ticket_reconciliation/', ticket_reconciliation_view, name="ticket_reconciliation"),
    path('ticket_reconciliation_create/',ticket_reconciliation_create_view, name = 'ticket_reconciliation_create'),
    path('ticket_reconciliation/<pk>/ticket_reconciliation_update/', TicketReconciliationUpdateView.as_view(), name = 'ticket_reconciliation_update'),
    path('ticket_reconciliation/<pk>/ticket_reconciliation_delete/',TicketReconciliationDeleteView.as_view(), name = 'ticket_reconciliation_delete'),
    #Trailer Attachment url
    path('trailer_attachment/', trailer_attachment_view, name="trailer_attachment"),
    path('trailer_attachment_create/',trailer_attachment_create_view, name = 'trailer_attachment_create'),
    path('trailer_attachment/<pk>/trailer_attachment_update/', TrailerAttachmentUpdateView.as_view(), name = 'trailer_attachment_update'),
    path('trailer_attachment/<pk>/trailer_attachment_delete/',TrailerAttachmentDeleteView.as_view(), name = 'trailer_attachment_delete'),
    #Insurance Validity url
    path('insurance_validity/', insurance_validity_view, name="insurance_validity"),
    path('insurance_risk_create/',insurance_risk_create_view, name = 'insurance_risk_create'),
    path('insurance_company_create/',insurance_company_create_view, name = 'insurance_company_create'),
    path('insurance_validity_create/',insurance_validity_create_view, name = 'insurance_validity_create'),
    path('insurance_validity/<pk>/insurance_risk_update/', InsuranceRiskUpdateView.as_view(), name = 'insurance_risk_update'),
    path('insurance_validity/<pk>/insurance_risk_delete/',InsuranceRiskDeleteView.as_view(), name = 'insurance_risk_delete'),
    path('insurance_validity/<pk>/insurance_company_update/', InsuranceCompanyUpdateView.as_view(), name = 'insurance_company_update'),
    path('insurance_validity/<pk>/insurance_company_delete/',InsuranceCompanyDeleteView.as_view(), name = 'insurance_company_delete'),
    path('insurance_validity/<pk>/insurance_validity_update/', InsuranceValidityUpdateView.as_view(), name = 'insurance_validity_update'),
    path('insurance_validity/<pk>/insurance_validity_delete/',InsuranceValidityDeleteView.as_view(), name = 'insurance_validity_delete'),
    #Driving Licence Validity url
    path('driving_licence_validity/', driving_licence_validity_view, name="driving_licence_validity"),
    path('driving_licence_validity_create/',driving_licence_validity_create_view, name = 'driving_licence_validity_create'),
    path('driving_licence_validity/<pk>/driving_licence_validity_update/', DrivingLicenceValidityUpdateView.as_view(), name = 'driving_licence_validity_update'),
    path('driving_licence_validity/<pk>/driving_licence_validity_delete/',DrivingLicenceValidityDeleteView.as_view(), name = 'driving_licence_validity_delete'),

]
