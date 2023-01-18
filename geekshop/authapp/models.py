from django.contrib.auth.models import AbstractUser
from django.db import models


# class ShopUser(User):
class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст',
                                      null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))