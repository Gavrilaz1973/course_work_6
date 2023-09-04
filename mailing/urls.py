from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import ClientListView, MessageListView, SettingsDetailView, MessageDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('users/', ClientListView.as_view(), name='users'),
    path('', MessageListView.as_view(), name='messages'),
    path('messages/<int:pk>/settings/', SettingsDetailView.as_view(), name='settings'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='messages_detail'),
]