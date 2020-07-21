from django.conf.urls import url
from cadenaEvolucion import views


urlpatterns = [
    url(r'^cadenaEvolucion/$', views.serie_list),
    url(r'^cadenaEvolucion/(?P<nombre>[\w-]+)/$', views.serie_pok)
]