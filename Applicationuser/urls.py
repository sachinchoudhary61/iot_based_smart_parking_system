from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from iot_based_smart_parking_system import settings
from django.conf.urls import url
from Applicationuser import views
from django.views.generic import TemplateView
urlpatterns = [
    # url(r'^reset-password$', views.reset_password),
    # url(r'^reset-password2$', views.reset_password1),
    url(r'^signup$', views.signup),

    # url(r'^book-slot', views.book),
    # url(r'^activeuser/$',views.verifyuser),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


