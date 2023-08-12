from django.db import models


class Advertisement(models.Model):

    #Название товара 
    title = models.CharField('заголовок', max_length=128)

    # Описание
    description = models.TextField('описание')

    # Цена
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'


    # Продавец
    # Фото объявления
    # Рейтинг
    # Актуальность