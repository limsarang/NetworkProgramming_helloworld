from django.contrib import admin
from django.urls import path

import playground.views

urlpatterns = [
    path('playground/hello/', playground.views.say_Hello),
    path('admin/', admin.site.urls),
]
