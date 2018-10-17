from django.db import models
from django.utils import timezone


class Category(models.Model):
    """カテゴリ名"""

    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    """投稿内容"""

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

