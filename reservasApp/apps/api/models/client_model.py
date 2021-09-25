from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=64)
    doc = models.CharField(max_length=15)
    doc_type = models.ForeignKey('DocType', on_delete=models.PROTECT)
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        unique_together = ['doc_type', 'doc']

    def __str__(self):
        return '{} => {}:{}, phone:{}'.format(
            self.full_name,
            self.doc_type,
            self.doc,
            self.phone
        )
