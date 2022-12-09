from django.urls import path
from . import views

urlpatterns = [
    path('', views.leads, name='leads'),
    path('<int:id>/', views.leads, name='leadDetails'),
    path('create/', views.createLead, name='createLead'),
    path('update/<int:id>', views.updateLead, name='updateLead'),
    path('delete/<int:id>', views.deleteLead, name='deleteLead'),
    path('convert/<int:id>', views.convertLead, name='convertLead'),
]