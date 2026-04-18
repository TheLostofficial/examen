from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Product(models.Model):
  UNITS_CHOICES = [
    ('piece.', 'шт.'),
    ('piece. (kit)', 'шт. (набор)'),
  ]

  article = models.CharField(max_length=20, unique=True, verbose_name='Артикул')
  name = models.CharField(max_length=100, verbose_name='Наименование товара')
  unit = models.CharField(max_length=20, default=UNITS_CHOICES, )
  prise = models.IntegerField(verbose_name='Цена (руб.)')
  brand = models.CharField(max_length=100, verbose_name='Кондитерская / Бренд')
  type = models.CharField(max_length=100, verbose_name='Тип торта')
  category = models.CharField(max_length=100, verbose_name='Категория торта')
  discount = models.IntegerField(default=0, verbose_name='Действующая скидка (%)')
  stock = models.IntegerField(verbose_name='Кол-во на складе (шт.)')
  descryption = models.TextField(blank=True, verbose_name='Описание товара')
  image = models.ImageField(upload_to='products/', blank=True, null=False, verbose_name='Фото')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'

class PickupPoint(models.Model):
  adress = models.CharField(max_length=200, verbose_name='Адресс пункта выдачи')

  def __str__(self):
    return self.adress

  class Meta:
    verbose_name = 'Пункт выдачи'
    verbose_name_plural = 'Пункты выдачи'

class Order(models.Model):

  STATUS_CHOICES = [
    ('new', 'Новый'),
    ('completed', 'Выполнен'),
  ]

  order_number = models.CharField(max_length=20, unique=True, verbose_name='Номер заказа')
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
  order_date = models.DateField(verbose_name='Дата заказа')
  delivery_date = models.DateField(verbose_name='Дата доставки')
  pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, verbose_name='Адресс пункта выдачи')
  pickup_code = models.ImageField(verbose_name='Код для получения')
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус заказа')

  def __str__(self):
    return f"Заказ {self.order_number} - {self.user.get_full_name()}"

  class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'

class Order_item(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item', verbose_name='Заказ')
  product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
  quantity = models.IntegerField(verbose_name='Количество')

  class Meta:
    verbose_name = 'Позиция заказа'
    verbose_name_plural = 'Позиции заказа'
    unique_together = ('order', 'product')

