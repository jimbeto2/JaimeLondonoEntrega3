
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'appbeto'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.LoginVista.as_view(), name='login'),
    #se pone el as_view pq LoginVista es una Clase y no una funcion
    path('logout/', LogoutView.as_view(template_name='appbeto/logout.html'), name='salida'),
    path('registro/', views.Registrarme.as_view(), name='registrar'),
    path('actualizar/', views.Actualizar.as_view(), name='actualizauser'),
    path('familiar/list/', views.familiar_list, name='familiar_listado'),
    path('familiar/form/', views.familiar_form, name='familiar_form'),
    path('familiar/editar/<int:indice>', views.familiar_editar, name='familiar_editar'),
    path('familiar/borrar/<int:indice>', views.familiar_borrar, name='familiar_borrar'),
    path('regalo/list/', views.regalo_list, name='regalo_listado'),
    path('regalo/form/', views.regalo_form, name='regalo_form'),
    path('menu/list/', views.menu_list, name='menu_listado'),
    path('menu/form/', views.menu_form, name='menu_form'),
]
