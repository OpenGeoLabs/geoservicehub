from django.db import models

# Create your models here.
class Process(models.Model):
    identifier = models.CharField(
            max_length=200,
            help_text="process identifier",
            blank=False
    )

    def __str__(self):
        return self.identifier
