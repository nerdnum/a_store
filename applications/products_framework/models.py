from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class ProductType(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    product_type = models.ForeignKey(ProductType, related_name='categories', blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}: {}'.format(self.product_type.name, self.name)

    class Meta:
        unique_together = ('product_type', 'name')
        ordering = ('product_type', 'name', )
        verbose_name_plural = 'categories'

class Attribute(models.Model):

    # Number, String, Date, Boolean, Integer, Binary, Timestamp, internet address
    # color, date, datetime - local, email, month, number, range, search, tel, time, url, week
    DATA_TYPES = (
        ('STRING', 'String'),
        ('INTEGER', 'Integer'),
        ('NUMBER', 'Number'),
        ('DATE', 'Date'),
        ('DATETIME', 'Datetime'),
        ('URL', 'Url'),
        ('EMAIL', 'Email'),
    )

    name = models.CharField(max_length=30, blank=False, null=False)
    product_type = models.ForeignKey(ProductType, related_name='attributes')
    data_type = models.CharField(max_length=8, choices=DATA_TYPES, default='STRING')
    required = models.BooleanField(default=False)
    is_active = models.BooleanField

    class Meta:
        ordering = ('product_type','name', )
        unique_together = ('product_type', 'name', )

    def __str__(self):
        return '{}: {}'.format(self.product_type.name, self.name)


