from django.urls import path
from . import views

urlpatterns = [

    path('', views.accounts, name='accounts'),
    path('<int:id>/', views.accounts, name='accountDetails'),
    path('create/', views.createAccount, name='createAccount'),
    path('update/<int:id>', views.updateAccount, name='updateAccount'),
    path('delete/<int:id>', views.deleteAccount, name='deleteAccount')

]