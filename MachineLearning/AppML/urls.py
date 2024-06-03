from django.urls import path, include
#from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home , name = "home"),
    path("datos", views.datos, name="datos"),
    path("prediccion", views.prediccion, name="prediccion"),
    
    #path("login", views.login, name="logine"),
    path("logout", views.exit, name="exit"),
    path("register", views.register, name="register"),
    
    path('formulario', views.mostrar_formulario, name='mostrar_formulario'),
    path('realizar_prediccion/', views.realizar_prediccion, name='realizar_prediccion'),
    
    path('redirect_repo/', views.redirect_repo, name='redirect_repo'),
    path('some-view/', views.some_view, name='some_view')
]
