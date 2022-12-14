from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    """Посты блога"""
    title = models.CharField('Заголовок', max_length=100)
    date = models.DateField('Дата поста', auto_now_add=True)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse_lazy('post'
                            , kwargs={'post_id': self.pk})
