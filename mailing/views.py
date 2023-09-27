from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory

from config import settings
from mailing.forms import MessageForm, ClientForm
from mailing.models import Client, Message


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')



