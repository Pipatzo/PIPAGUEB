from django.contrib import admin

# Register your models here.
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
