from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from iot_based_smart_parking_system import settings
urlpatterns = [


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
