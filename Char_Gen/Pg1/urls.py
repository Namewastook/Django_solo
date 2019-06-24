from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('created_char/', views.created_char, name="created_char"),
    path('random_char/', views.random_char, name="random_char"),
    path('verify_data/', views.verify_data, name="verify_data"),
    path("die_roller/", views.die_roller, name="die_roller")
]
