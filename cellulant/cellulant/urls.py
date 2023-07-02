from django.contrib import admin
from django.urls import path
from .views import cellulant_api_endpoint


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('api/endpoint/', cellulant_api_endpoint, name='cellulant_api_endpoint'),
]
