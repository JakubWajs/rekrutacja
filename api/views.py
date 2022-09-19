from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView

from api.models import Link
from api.serializer import LinkSerializer


class ShortenListView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShorterCreateView(CreateAPIView):
    serializer_class = LinkSerializer


class RedirectorView(View):
    def get(self, request, *args, **kwargs):
        short_link = f'{settings.HOST_URL}/{self.kwargs["short_link"]}'
        source_link = get_object_or_404(Link, short_link=short_link).source_link

        return redirect(source_link)
