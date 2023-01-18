from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('категория товара', max_length=64)
    description = models.TextField('описание', blank=True)
    is_active = models.BooleanField('активность', default=True)

    class Meta:
        verbose_name = 'категория товаров'
        verbose_name_plural = 'категории товаров'
        ordering = ['name']

    def __str__(self):
        return f'Категория {self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField('имя', max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField('описание', blank=True)
    short_desc = models.CharField('краткое описание', max_length=64, blank=True)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
    is_active = models.BooleanField('активность', default=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.name} ({self.category.name})'
