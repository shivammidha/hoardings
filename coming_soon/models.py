from django.db import models


class Clients(models.Model):
    email_address = models.EmailField(unique=True, blank=True)
