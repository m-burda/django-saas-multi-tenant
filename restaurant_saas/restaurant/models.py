from django.db import models
from tenant.models import Tenant


# class RestaurantModel(models.Model):
#     tenant = models.OneToOneField(
#         Tenant,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=100, blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.name} ({self.tenant})'


class MenuModel(models.Model):
    restaurant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, default=f'{restaurant} Menu')

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.menu} category: {self.name}'


class MenuItemModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}: {self.name}'
