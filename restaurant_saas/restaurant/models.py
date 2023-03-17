from django.db import models
from tenant.models import Tenant


class MenuModel(models.Model):
    restaurant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, default=f"{restaurant} Menu")

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE, related_name='category_set')

    def __str__(self):
        return f"{self.menu} category: {self.name}"


class MenuItemModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='item_set')

    def __str__(self):
        return f"{self.category}: {self.name}"
