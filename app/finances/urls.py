from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income, name='income'),
    path('outcome/', views.outcome, name='outcome'),
    path('statistics/', views.statistics, name='statistics'),
    path('add_income/', views.add_income, name='add_income')
]
