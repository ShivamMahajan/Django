from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.register_user, name='register_user'),
    url(r'^email/', views.get_email, name='get_email'),
    url(r'^email_save/', views.get_email_save, name='get_email_save'), 
]