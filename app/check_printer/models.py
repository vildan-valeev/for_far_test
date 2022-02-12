from django.db import models

CHECK_TYPE = [
    ('kitchen', 'Kitchen'),
    ('client', 'Client'),
]
CHECK_STATUS = [
    ('new', 'New'),
    ('rendered', 'Rendered'),  # check create_pdf_check.py before edit
    ('printed', 'Printed'),
]


class Check(models.Model):
    """
    Чеки
    """
    printer_id = models.ForeignKey('Printer', on_delete=models.PROTECT, verbose_name='Принтер')
    type = models.CharField(max_length=50, choices=CHECK_TYPE, verbose_name='Тип')
    order = models.JSONField(verbose_name='Заказ', help_text='Информация о заказе')
    status = models.CharField(max_length=50, choices=CHECK_STATUS, default='new', verbose_name='Статус', help_text='Статус чека')
    pdf_file = models.FileField(verbose_name='Ссылка', help_text='ссылка на созданный PDF-файл', null=True, blank=True)

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'

    def __str__(self):
        return f'{self.id} {self.printer_id} {self.printer_id}'


class Printer(models.Model):
    """
    Принтеры
    """
    name = models.CharField(max_length=100, verbose_name='Имя', help_text='название принтера')
    api_key = models.CharField(unique=True, max_length=100, verbose_name='Ключ', help_text='ключ доступа к API')
    check_type = models.CharField(max_length=100, choices=CHECK_TYPE, verbose_name='Тип',
                                  help_text='тип чека которые печатает принтер')
    point_id = models.IntegerField(verbose_name='ID точки',
                                   help_text='точка к которой привязан принтер')

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return f'{self.id} {self.name}'
