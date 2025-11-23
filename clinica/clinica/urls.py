from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # urls principais da api, ex: /api/pacientes/
    path('api/', include('api.urls')),
    
    # url para obter o token de login 
    path('api-login/', authtoken_views.obtain_auth_token), 
]