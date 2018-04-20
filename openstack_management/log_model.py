from django.db import models

class SystemLog(models.Model):
    error_type
    error_message
    error_action
    error_from
    error_creator
