"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from watchlist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('watchlist/',views.watchlist, name='watchlist'),
    path('watchlist/create/',views.create_watchlist, name='create_watchlist'),
    path('watchlist/<int:elem_id>',views.puntuar, name='review'),    
    path('contacto/',views.enviar_mensaje, name='contacto'),
    path('watchlist/<int:elem_id>/sacar',views.sacar_listado, name='sacar_listado'),    
    path('logout/',views.cerrar_sesion, name='logout'),
    path('signin/',views.iniciar_sesion, name='signin'),
    ]
