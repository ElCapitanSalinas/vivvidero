from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('newhouse/', views.createhouse, name='create'),
    path('newhouse/create/', views.newhouse, name='new_house'),
    path('newhouse/images/', views.uploadimgs, name='imgs'),
    path('newhouse/final/', views.finalview, name='pdfgen'),
    path('newhouse/final/pdf/', views.verpdf, name='verpdf'),
    path('admin/', views.admin, name='admin'),
    path('admin/viewgallery/', views.admview, name='admin'),
    path('admin/register/', views.adminreg, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)