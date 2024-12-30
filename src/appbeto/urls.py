
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'appbeto'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='sobremi'),
    path('login/', views.LoginVista.as_view(), name='login'),
    #se pone el as_view pq LoginVista es una Clase y no una funcion
    path('logout/', LogoutView.as_view(template_name='appbeto/logout.html'), name='salida'),
    path('registro/', views.Registrarme.as_view(), name='registrar'),
    path('actualizar/', views.Actualizar.as_view(), name='actualizauser'),
    path('misblog_editar/<int:indice>', views.MisBlog_edit, name='misblog_edit'),
    path('misblog/borrar/<int:indice>', views.MisBlog_borrar, name='misblog_borrar'),
    path('misblog/crear/', views.MisBlog_crear, name='misblog_crear'),

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
