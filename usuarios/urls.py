from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name='logar'),
    path('exames/', include('exames.urls')),
]