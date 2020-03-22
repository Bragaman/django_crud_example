from rest_framework.viewsets import ModelViewSet

from mail.models import Mail
from mail import serializers


class MailViewSet(ModelViewSet):
    queryset = Mail.objects.all()

    def get_serializer_class(self):
        serializer_class = serializers.MailSerializer

        if self.request.method in ('PUT', 'PATCH'):
            serializer_class = serializers.MailUpdateSerialiser

        return serializer_class
