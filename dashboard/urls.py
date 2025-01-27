from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.app, name="app"),
    path("test/<str:slug>", views.test, name="test"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
