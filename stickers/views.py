from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView
)
from .models import Sticker


class StickersHome(ListView):
    model = Sticker
    context_object_name = 'stickers'
    template_name = 'stickers/home.html'

    def get_queryset(self):
        data = Sticker.objects.all()
        return data