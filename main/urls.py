from django.urls import path
from django.conf.urls import url
from .views import ProductsListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", ProductsListView.as_view(), name="home"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)