from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('info_decemb', views.info_decemb, name='info_decemb'),
    path('info_borod', views.info_borod, name='info_borod'),
    path('info_polt', views.info_polt, name='info_polt'),
    path('info_plague', views.info_plague, name='info_plague'),
    path('info_salt', views.info_salt, name='info_salt'),
    path('info_solovki', views.info_solovki, name='info_solovki'),
    path('info_razin', views.info_razin, name='info_razin'),
    path('info_copper', views.info_copper, name='info_copper'),
    path('info_gangut', views.info_gangut, name='info_gangut'),
    path('info_pugach', views.info_pugach, name='info_pugach'),
    path('info_izmail', views.info_izmail, name='info_izmail'),
    path('info_sevast', views.info_sevast, name='info_sevast'),
    path('info_shamil', views.info_shamil, name='info_shamil'),
    path('info_sinop', views.info_sinop, name='info_sinop'),
    path('info_brus', views.info_brus, name='info_brus'),
    path('info_octob', views.info_octob, name='info_octob'),
    path('info_stalg', views.info_stalg, name='info_stalg'),
    path('info_tsush', views.info_tsush, name='info_tsush'),
    path('info_klush', views.info_klush, name='info_klush'),
    path('info_chigir', views.info_chigir, name='info_chigir'),
    path('info_azov', views.info_azov, name='info_azov'),
    path('info_grsegs', views.info_grsegs, name='info_grsegs'),
    path('info_lesn', views.info_lesn, name='info_lesn'),
    path('info_maloyr', views.info_maloyr, name='info_maloyr'),
    path('info_smolnsk1609', views.info_smolnsk1609, name='info_smolnsk1609'),
    path('info_chesm', views.info_chesm, name='info_chesm'),
    path('info_tarut', views.info_tarut, name='info_tarut'),
    path('info_smolnsk1812', views.info_smolnsk1812, name='info_smolnsk1812'),
    path('info_leipz', views.info_leipz, name='info_leipz'),
    path('info_aust', views.info_aust, name='info_aust'),
    path('info_berl', views.info_berl, name='info_berl'),
    path('info_blokl', views.info_blokl, name='info_blokl'),
    path('info_rzhev', views.info_rzhev, name='info_rzhev'),
    path('info_galic', views.info_galic, name='info_galic'),
]
