from django.db import models
from apps.api.models.car_type_model import CarType
from apps.api.models.doc_type_model import DocType
from apps.api.models.client_model import Client
from apps.api.models.revision_type_model import RevisionType


class Reserve(models.Model):
    id = models.AutoField(primary_key=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    date = models.DateField()
    hour = models.TimeField()
    plate = models.CharField(max_length=6, blank=False)
    ended = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    car_type = models.ForeignKey('CarType', on_delete=models.PROTECT)
    rev_type = models.ForeignKey('RevisionType', on_delete=models.PROTECT)
    owner = models.ForeignKey(
        'Client', on_delete=models.PROTECT, related_name='r_as_owner')
    driver = models.ForeignKey(
        'Client', on_delete=models.PROTECT, related_name='r_as_driver')

    class Meta:
        verbose_name = 'Reserv'
        verbose_name_plural = 'Reserves'
        ordering = ['id']

    def __str__(self):
        return '{} => {}:{}, Owner:{}, Driver:{}'.format(
            self.plate,
            self.date,
            self.hour,
            self.owner,
            self.driver
        )
