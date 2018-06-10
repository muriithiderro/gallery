from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('personal.urls')),
    url(r'^admin/', admin.site.urls)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
