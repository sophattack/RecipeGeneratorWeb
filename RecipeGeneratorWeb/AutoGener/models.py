from django.db import models

# Create your models here.
class CanDo(models.Model):
    """ the meal user can do"""
    TYPE_CHOICES = (
        ('荤', '荤'),
        ('素', '素'),
        ('both', 'both'),
        ('暂不选择', '暂不选择'),
        ('主食', '主食')
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='暂不选择')

    def __str__(self):
        return self.name


class CanGet(models.Model):
    """ the ingredients user can get"""
    name = models.CharField(max_length=100)
    cal = models.PositiveIntegerField(help_text="千卡/100g")

    def __str__(self):
        return self.name
