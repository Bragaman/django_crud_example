from rest_framework import serializers

from mail.models import Mail


class MailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mail
        fields = '__all__'
        read_only_fields = [
            'created_at',
            'unread',
        ]


class MailUpdateSerializer(MailSerializer):

    class Meta(MailSerializer.Meta):
        read_only_fields = [
            'user_from',
            'user_to',
            'subject',
            'text',
            'created_at',
        ]
