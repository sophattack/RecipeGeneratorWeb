from django.db import models

# Create your models here.

class CanGet(models.Model):
    """ the ingredients user can get"""
    name = models.CharField(max_length=10)
    cal = models.PositiveIntegerField()

    def __str__(self):
        return self.name


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
    ingre = models.ManyToManyField(CanGet, blank=True)

    def __str__(self):
        return self.name


# class Compose(models.Model):
#     dish = models.ForeignKey(CanDo, models.PROTECT)
#     ingre = models.ForeignKey(CanGet, models.PROTECT)
#
#     def __str__(self):
#         return self.dish.name
