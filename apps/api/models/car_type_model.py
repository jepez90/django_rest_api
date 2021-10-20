from django.db import models


class CarType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Car Type'
        verbose_name_plural = 'Car Types'
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)
