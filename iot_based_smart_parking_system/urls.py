"""iot_based_smart_parking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from iot_based_smart_parking_system import settings
from django.conf.urls import url
from Applicationuser import views
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('sps_mgmt/', include('parkingmanagement.urls')),
    path('user/', include('Applicationuser.urls'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,documnet_root = settings.MEDIA_ROOT)
