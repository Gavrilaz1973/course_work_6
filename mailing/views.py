from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mailing.models import Client, Message, Settings


class ClientListView(ListView):
    model = Client


class SettingsDetailView(DetailView):
    model = Settings


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message



