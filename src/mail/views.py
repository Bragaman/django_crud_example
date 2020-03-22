import copy

from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mail.models import Mail
from mail import serializers


class MailViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Mail.objects.all()

    def get_serializer_class(self):
        serializer_class = serializers.MailSerializer

        if self.request.method in ('PUT', 'PATCH'):
            serializer_class = serializers.MailUpdateSerializer

        return serializer_class

    def get_queryset(self):
        # переопределяем, чтобы избавиться действия PUT, PATCH, GET
        # мог совершать только тот пользватель, что отправил или получил письма
        user = self.request.user
        return self.queryset.filter(Q(user_from=user) | Q(user_to=user))

    def create(self, request, *args, **kwargs):
        # Переопредяем методсоздания, чтобы нельзя было создать email от чужого имени
        data = copy.deepcopy(request.data)
        # игнорируем, то что пришло от пользователя в этом поле
        data["user_from"] = self.request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)