from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals, name='deals'),
    path('<int:id>/', views.deals, name='dealDetails'),
    path('create/', views.createDeal, name='createDeal'),
    path('update/<int:id>', views.updateDeal, name='updateDeal'),
    path('delete/<int:id>', views.deleteDeal, name='deleteDeal'),
]