from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

app_name = 'rango'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)