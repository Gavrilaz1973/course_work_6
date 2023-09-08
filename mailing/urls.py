from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import ClientListView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create', ClientCreateView.as_view(), name='clients_create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='clients_detail'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='clients_delete'),
    path('', MessageListView.as_view(), name='messages'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='messages_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='messages_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='messages_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='messages_delete'),
]