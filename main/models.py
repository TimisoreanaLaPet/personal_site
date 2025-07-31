from django.db import models

SALUTATION_CHOICES = [
    ('mr', 'Mr.'),
    ('ms', 'Ms.'),
    ('dr', 'Dr.'),
]

class Subscriber(models.Model):
    salutation = models.CharField(max_length=5, choices=SALUTATION_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
