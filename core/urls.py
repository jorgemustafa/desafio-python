from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.viewsets import PacientesViewSet, ExamesViewSet

route = routers.DefaultRouter()
route.register('pacientes', PacientesViewSet, basename='Pacientes')
route.register('exames', ExamesViewSet, basename='Exames')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
