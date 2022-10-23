from cgitb import text
from ipaddress import ip_address
from django.db import models

# Create your models here.

class WS_address(models.Model):
    """Wyrestorm address"""
    ws_ip = models.GenericIPAddressField()
    loc = models.CharField(max_length=200)
    
    