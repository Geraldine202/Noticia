from django.urls import path, include
from .views import *
from rest_framework import routers
from django.contrib.auth import views as auth_views

#CONFIGURACION PARA EL API
router = routers.DefaultRouter()
router.register('categorias',CategoriaViewset)
router.register('noticias',NoticiaViewset)
router.register('periodistas',PeriodistaViewset)

urlpatterns = [
    path('',index,name="index"),
    path('noticias/',noticias,name="noticias"),
    path('noticias/add/',noticiasadd,name="noticiasadd"),
    path('noticias/update/<id>/',noticiasupdate,name="noticiasupdate"),
    path('noticias/delete/<id>/',noticiasdelete,name="noticiassdelete"),
    path('noticias/soliciupdate/<id>/',soliupdate,name="soliupdate"),
    path('noticias/solisadd/',solicsadd,name="solicsadd"),


    path('periodistas/',periodistas,name="periodistas"),
    path('periodistas/add/',periodistasadd,name="periodistasadd"),
    path('periodistas/update/<id>/',periodistasupdate,name="periodistasupdate"),
    path('periodistas/delete/<id>/',periodistasdelete,name="periodistasdelete"),
    path('cultura/',cultura,name="cultura"),
    path('deportes/',deportes,name="deportes"),
    path('internacional/',internacional,name="internacional"),
    path('contacto/',contacto,name="contacto"),
    path('economia/',economia,name="economia"),
    path('monja/',monja,name="monja"),
    path('servicios/',servicios,name="servicios"),
    path('voucher/',voucher,name="voucher"),
    path('historial_pago/', historial_pago, name="historial_pago"),
    path('register/',register,name="register"),
    path('solicitud/',solicitud,name="solicitud"),
    path('galeria/',galeria,name="galeria"),
    
    #API
    path('api/',include(router.urls)),
    path('periodistasapi/',periodistasapi,name="periodistasapi"),
    path('periodistadetalle/<id>/',periodistadetalle,name="periodistadetalle"),


    path('account_locked/',account_locked,name="account_locked"),
    path('password_change_form/',password_change_form,name="password_change_form"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

