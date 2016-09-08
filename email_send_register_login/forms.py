from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django import forms
    
class Email(models.Model):
    subject = models.CharField('Subject', max_length=200)
    contact_email = models.CharField('Mail To', max_length=100)
    content = models.CharField('Content', max_length=400)
    def __str__(self):
        return self.contact_email

class insert(models.Model):
    user_name = models.CharField('User name', max_length=80)
    email_name = models.CharField('Email', max_length=100)
    password = models.CharField('Password', max_length=100)
    # subject = models.CharField('Subject', max_length=200)
    # contact_email = models.CharField('Mail To', max_length=100)
    def __str__(self):
        return self.user_name

  