from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^signup_success/$', views.signup_success, name='signup-success'),
    #url(r'^ajax/validate_username/$', views.validate_username, name='validate_username')
]