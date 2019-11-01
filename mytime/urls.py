from django.urls import path

app_name = 'mytime'

from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('time/',views.get_time,name='get_time'),
]