from django.db import models


class ProductCategory(models.Model):
#(типы полей)
#https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории продуктов'
        verbose_name_plural = 'Категории продуктов'


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

#Методы которые возвращают QuerySets
#https: // docs.djangoproject.com / en / 4.2 / ref / models / querysets /  # methods-that-return-new-querysets