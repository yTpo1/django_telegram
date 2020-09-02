from django.urls import path
from . import views

# app_name = 'channels'
urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='channels-home'),
    path('add-channel/', views.add_channel, name='channels-add'),
    path('about/', views.about, name='channels-about'),
    path('contact/', views.contact, name='channels-contact'),
    path('channel/category/<str:name>', views.ChannelListView.as_view(), name='channels-category'),
    path('channel/<int:pk>', views.ChannelDetailView.as_view(), name='channel-detail'),
]
