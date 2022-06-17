from django.db import models


class TimeStampedModel(models.Model):

    """ Timestamp Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
