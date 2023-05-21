from django.contrib import admin
from django.urls import path
from CLIENT_LearnFS import views as client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client_views.main),
]