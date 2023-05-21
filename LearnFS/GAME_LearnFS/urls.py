from django.contrib import admin
from django.urls import path
from GAME_LearnFS import views as game_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_views.main),
]