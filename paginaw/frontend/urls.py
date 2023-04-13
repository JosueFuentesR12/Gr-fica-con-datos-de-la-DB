from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('chart', views.chart, name="chart"),
    path('log', views.log, name="log"),
    path('index', views.index, name="index"),
]