from django.db import models

# Create your models here.


class CsvUpload(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="media/")

    def __str__(self):
        return self.name


class SortedCsv(models.Model):
    rank = models.IntegerField()
    # teacher = models.CharField(max_length=100)
    # subject = models.CharField(max_length=100)
    # experience = models.IntegerField()
    # technical_quality = models.FloatField()