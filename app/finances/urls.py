from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income, name='income'),
    path('add_income/', views.add_income, name='add_income'),
    path('outcome/', views.outcome, name='outcome'),
    path('outcome/add_category', views.add_category, name='add_category'),
    path('outcome/<category_name>', views.category, name='category'),
    path('statistics/', views.statistics, name='statistics')
]
