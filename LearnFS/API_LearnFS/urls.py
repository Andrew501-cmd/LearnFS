from django.contrib import admin
from django.urls import include, path
from API_LearnFS import views as api_views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_views.documentation),
    path('v1/allList', api_views.V1_allList.as_view()),
    path('v2/allList', api_views.V2_allList.as_view()),
    path('v1/getArticle', getArticle.as_view()),
    path('v1/searchArticle', searchArticle.as_view()),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)