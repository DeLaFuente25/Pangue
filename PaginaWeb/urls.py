
from django.contrib import admin
from django.urls import path
from pangue.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),

]
