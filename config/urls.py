from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Academica.views import listaPacientes, listaCamas, listaPlantas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listaPacientes, name='inicio'),
    path('pacientes/', listaPacientes, name='listado_pacientes'),
    path('camas/', listaCamas, name='listado_camas'),
    path('plantas/', listaPlantas, name='listado_plantas'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
