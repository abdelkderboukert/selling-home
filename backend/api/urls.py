from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('predict/', predict_view, name='predict'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)