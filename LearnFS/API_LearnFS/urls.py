from django.contrib import admin
from django.urls import path
from API_LearnFS import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_views.documentation),
]