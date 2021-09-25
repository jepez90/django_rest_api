from django.db import models


class DocType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=1)
    short = models.CharField(max_length=5)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Document Type'
        verbose_name_plural = 'Document Types'
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)
