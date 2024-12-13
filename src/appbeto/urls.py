
from django.urls import path
from . import views

app_name = 'appbeto'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('familiar/list', views.familiar_list, name='familiar_list'),
    path('familiar/form', views.familiar_form, name='familiar_form'),
    path('regalo/list', views.regalo_list, name='regalo_list'),
    path('regalo/form', views.regalo_form, name='regalo_form'),
    path('menu/list', views.menu_list, name='menu_list'),
    path('menu/form', views.menu_form, name='menu_form'),
]
