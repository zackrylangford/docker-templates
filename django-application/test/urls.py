#URLs for test app
from . import views
from django.urls import path



app_name = 'test'


#URLs for test app
urlpatterns = [
    path('', views.index, name='index'),

]