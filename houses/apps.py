from django.apps import AppConfig

import smtplib, ssl

class HousesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'
    # def ready(self):