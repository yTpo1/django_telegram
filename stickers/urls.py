from django.urls import path

from . import views
from .views import StickersHome

urlpatterns = [
    path('', StickersHome.as_view(), name='stickers-home'),
]