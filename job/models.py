from django.db import models
from process.models import Process
from pywps.response.status import STATUS


# Create your models here.
class Job(models.Model):

    STATUS_CHOICES = (
        (STATUS.ERROR_STATUS, "Error"),
        (STATUS.NO_STATUS, "No status"),
        (STATUS.STORE_STATUS, "Store"),
        (STATUS.STORE_AND_UPDATE_STATUS, "Store and update"),
        (STATUS.DONE_STATUS, "Done"),
    )

    uuid = models.CharField(
            primary_key=True,
            max_length=255,
            blank=False,
            unique=True)

    pid = models.IntegerField(
            blank=False,
            unique=False)


    operation = models.CharField(
            max_length=30,
            null=False)

    version = models.CharField(
                max_length=5
            )

    time_start = models.DateTimeField()

    time_end = models.DateTimeField()

    message = models.TextField()

    percent_done = models.FloatField()

    status = models.IntegerField(choices=STATUS_CHOICES)

    identifier = models.CharField(
            max_length=255)

    class Meta:
        managed = False
        db_table = 'pywps_requests'


    def __str__(self):
        return ("{} - {}".format(self.uuid, self.identifier))
