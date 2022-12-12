from django.db import models


class Project(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    discription = models.CharField('Описание', max_length=255)
    image = models.ImageField('Изображение', upload_to='portfolio/images/')
    url = models.URLField('URL', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'