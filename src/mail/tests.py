from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from mail.models import Mail


class MailTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MailTestCase, cls).setUpClass()
        user_model = get_user_model()
        cls.users = []
        cls.clients = []
        for i in range(3):
            name = str(i)
            cls.users.append(user_model.objects.create_user(
                username=name,
                email=name + "@live.com",
                password=name
            ))
            client = APIClient()
            client.login(username=name, password=name)
            cls.clients.append(client)

        for i in range(2):
            Mail.objects.create(
                user_from=cls.users[0],
                user_to=cls.users[1],
                subject="test",
                text="test"
            )

    def test_no_auth(self):
        client = APIClient()
        r = client.get(
            '/api/mails/'
        )
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

    def _test_get(self, client, expected_mails_count):
        r = client.get('/api/mails/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data["count"], expected_mails_count)

    def test_get(self):
        for i, count in enumerate([2, 2, 0]):
            self._test_get(self.clients[i], count)

    def test_create(self):
        client = self.clients[2]
        queryset = Mail.objects.filter(user_from=self.users[2])
        self.assertEqual(queryset.count(), 0)
        r = client.post('/api/mails/', data={
            # поле должно быть проигнорированно
            "user_from": self.users[0].pk,
            "user_to": self.users[0].pk,
            "subject": "test",
            "text": "test",
        })
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(queryset.count(), 1)

    def test_put(self):
        client = self.clients[1]
        mail = Mail.objects.filter(user_to=self.users[1]).first()
        r = client.put('/api/mails/{}/'.format(mail.pk), data={
            "unread": False,
        })
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        updated_mail = Mail.objects.get(pk=mail.pk)
        self.assertEqual(updated_mail.unread, False)
        self.assertEqual(updated_mail.created_at, mail.created_at)

    def test_put_invalid(self):
        client = self.clients[0]
        mail = Mail.objects.exclude(user_to=self.users[0]).first()
        r = client.put('/api/mails/{}/'.format(mail.pk), data={
            "unread": False,
        })
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        client = self.clients[1]
        mail = Mail.objects.filter(user_to=self.users[1]).first()
        r = client.delete('/api/mails/{}/'.format(mail.pk), data={
            "unread": False,
        })
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mail.objects.filter(pk=mail.pk).count(), 0)
