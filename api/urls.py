from django.urls import path

from api.views import ShortenListView, ShorterCreateView

urlpatterns = [
    path('all_links/', ShortenListView.as_view(), name='all_links'),
    path('create/', ShorterCreateView.as_view(), name='create'),
]
