from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from uploads.views import image_upload

urlpatterns = [
    path("uploads/", image_upload, name="uploads"),
    path('admin/', admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
