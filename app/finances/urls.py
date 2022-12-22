from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('', views.index, name='index'),
    path('income/', views.income, name='income'),
    path('income/add_income/', views.add_income, name='add_income'),
    path('outcome/', views.outcome, name='outcome'),
    path('outcome/add_category/', views.add_category, name='add_category'),
    path('outcome/<category_name>/', views.category, name='category'),
    path('outcome/<category_name>/<int:category_id>/',
         views.add_outcome, name='add_outcome'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/income/', views.statistics_income, name='stat_income'),
    path('statistics/income/show',
         views.show_income, name='show_income'),
    path('statistics/outcome/', views.statistics_outcome, name='stat_outcome'),
    path('statistics/outcome/show',
         views.show_outcome, name='show_outcome'),
]
