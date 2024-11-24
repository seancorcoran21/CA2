from django.urls import path
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
] 
