from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from mail import views

router = routers.DefaultRouter()
router.register(r'mails/?', views.MailViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
