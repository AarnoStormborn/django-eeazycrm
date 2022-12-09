from django.urls import path
from . import views
urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('<int:id>/', views.contacts, name='contactDetails'),
    path('create/', views.createContact, name='createContact'),
    path('update/<int:id>', views.updateContact, name='updateContact'),
    path('delete/<int:id>', views.deleteContact, name='deleteContact'),
]