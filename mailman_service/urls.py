from django.urls import include, path

from mailman_service.views import EmailView, CreateUserView


urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('email/', EmailView.as_view(), name='send_email'),
]

