from django.db import models

class Homeblocks(models.Model):
    title = models.CharField('Заголовок', max_length=50, default='Заголовок', help_text='Введите значение')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок информации на главной'
        verbose_name_plural = 'Блоки с информацией на главной'

class Demand(models.Model):
    title = models.CharField('Название таблицы', max_length=50, default="")
    html_table = models.TextField('HTML таблица', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Востребованность (таблицы)'
        verbose_name_plural = 'Востребованность (таблицы)'

class Chart(models.Model):
    title = models.CharField('Название таблицы', max_length=50)
    image = models.ImageField("График", upload_to="charts/", default="")
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE, verbose_name="График")

class Geo(models.Model):
    title = models.CharField('Название таблицы', max_length=50, default="")
    html_table = models.TextField('HTML таблица', default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'География (таблицы)'
        verbose_name_plural = 'География (таблицы)'

class Chart2(models.Model):
    title = models.CharField('Название таблицы', max_length=50)
    image = models.ImageField("График", upload_to="charts/", default="")
    geo = models.ForeignKey(Geo, on_delete=models.CASCADE, verbose_name="График")

class Topskills(models.Model):
    title = models.CharField('Название таблицы', max_length=50, default="")
    html_table = models.TextField('HTML таблица', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навыки (таблицы)'
        verbose_name_plural = 'Навыки (таблицы)'

class Chart3(models.Model):
    title = models.CharField('Название таблицы', max_length=50)
    image = models.ImageField("График", upload_to="charts/", default="")
    topskills = models.ForeignKey(Topskills, on_delete=models.CASCADE, verbose_name="График")
