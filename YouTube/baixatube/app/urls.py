from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... seus URLs aqui
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)