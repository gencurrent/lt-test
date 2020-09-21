from pathlib import Path

from django.db import models
from django.conf import settings


class Branch(models.Model):
    '''
    A branch to attach employees to
    Uses Google Map in admin panel to manipulate latitude and longitude
    '''
    FACADE_IMAGE_PATH = Path(settings.MEDIA_ROOT) / 'organization' / 'facade_image'

    name = models.CharField('Name', max_length=40, null=False, blank=True, default='', )
    facade_image = models.ImageField('Facade image', null=False, default='', upload_to=str(FACADE_IMAGE_PATH))
    latitude = models.DecimalField(
        'Latitude',
        max_digits=9, 
        decimal_places=6, 
        null=True, blank=True
    )
    longitude = models.DecimalField(
        'Longitude',
        max_digits=9, 
        decimal_places=6, 
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
    

class Employee(models.Model):
    '''
    A simple employee model
    '''
    first_name = models.CharField('First Name', max_length=40, null=False, blank=True, default='')
    third_name = models.CharField('Third Name', max_length=40, null=False, blank=True, default='')
    position_title = models.CharField('Position Title', max_length=40, null=False, blank=True, default='')
    branch = models.ForeignKey(
        Branch,
        verbose_name='Branch', on_delete=models.CASCADE,
        null=True, blank=True, default=None,
        related_name='employee_list'
    )

    def __str__(self):
        return f'{self.first_name} {self.third_name}'

    