from django.db import models


class RevisionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Revision Type'
        verbose_name_plural = 'Revision Type'
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)
