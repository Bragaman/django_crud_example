from django.conf.urls import url

from users import views


urlpatterns = [
    url('signup', views.UserRegistrationView.as_view()),
]
