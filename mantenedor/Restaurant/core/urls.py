from django.urls import path  
from .views import home,form_plato,form_mod_plato,form_del_plato,form_reserva,form_mod_reserva,form_del_reserva,reserva,form_bodega,form_del_bodega,form_mod_bodega,bodega


urlpatterns =[
    path('',home,name="home"),
    path('form-plato',form_plato,name='form_plato'),
    path('form-mod-plato/<id>',form_mod_plato,name='form_mod_plato'),
    path('form-del-plato/<id>',form_del_plato,name='form_del_plato'),


    path('reserva',reserva,name="reserva"),
    path('form-reserva',form_reserva,name='form_reserva'),
    path('form-mod-reserva/<id>',form_mod_reserva,name='form_mod_reserva'),
    path('form-del-reserva/<id>',form_del_reserva,name='form_del_reserva'),

    path('bodega',bodega,name="bodega"),
    path('form-bodega',form_bodega,name='form_bodega'),
    path('form-mod-bodega/<id>',form_mod_bodega,name='form_mod_bodega'),
    path('form-del-bodega/<id>',form_del_bodega,name='form_del_bodega'),
]