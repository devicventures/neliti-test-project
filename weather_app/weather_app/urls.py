
from django.contrib import admin
from django.urls import path
from weather_finder.views import home, get_data, weather

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', home, name='home'),
    path('weather/', weather, name='weather'),

    
    path('data/', get_data.as_view(), name='api-data'),

]
