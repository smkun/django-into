from django.urls import path
from . import views


urlpatterns = [
    path('api/contacts', views.ContactList.as_view(), name='contact_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/contacts/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('companies/', views.company_list, name='company_list'),
    path('companies/add/', views.company_add, name='company_add'),
    path('companies/edit/<int:company_id>/', views.company_edit, name='company_edit'),
    path('companies/delete/<int:company_id>/', views.company_delete, name='company_delete'),
]