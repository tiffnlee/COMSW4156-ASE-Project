from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import RegexValidator

import datetime

TEAM_CHOICES = (
    ('DUOS', 'DUOS'),
    ('SQUADS', 'SQUADS'),
    ('DUOS FPS', 'DUOS FPS'),
    ('SQUADS FPS', 'SQUADS FPS')
)

REGION_CHOICES = (
    ('NA', 'North America'),
    ('EU', 'Europe'),
    ('AS', 'Asian'),
    ('OC', 'Oceania'),
    ('SA', 'South America'),
    ('SEA', 'South East Asia'),
    ('KR/JP', 'Korea/Japan')
)

class Search(models.Model):
    alphanumeric = RegexValidator('^[A-Za-z0-9]+$', message="Password should be a combination of Alphabets and Numbers")
    user_id = models.CharField(max_length=20, validators=[alphanumeric])
    steam_id = models.CharField(max_length=20)
    team_choices = models.CharField('team preference', max_length=10, choices=TEAM_CHOICES)
    region_choices = models.CharField('region preference', max_length=5, choices=REGION_CHOICES)
    email = models.EmailField('email')
    has_profile = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined', default=timezone.now)	

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
