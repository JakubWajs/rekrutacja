from django.contrib import admin
from django.urls import path, include
from api.views import RedirectorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('<str:short_link>/', RedirectorView.as_view(), name='redirector'),
]
