from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('first/', include('first.urls')),
    path('', include('first.urls')),
    path('admin/', admin.site.urls),
]
