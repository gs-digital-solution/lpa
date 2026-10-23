from django.contrib import admin
from django.urls import path, include
from django.conf import settings as dj_settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if dj_settings.DEBUG:
    urlpatterns += static(dj_settings.MEDIA_URL, document_root=dj_settings.MEDIA_ROOT)