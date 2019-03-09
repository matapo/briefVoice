from django.urls import path

from dialogflow_webhook import webhook

urlpatterns = [
    path('serve', webhook.serve, name='serve'),
]