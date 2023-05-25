from django.contrib import admin
from django.urls import path
from API_LearnFS import views as api_views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_views.documentation),
    path('v1/allList', V1_allList),
]