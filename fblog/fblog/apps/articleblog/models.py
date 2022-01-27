import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class Article(models.Model):
    blog_titles = models.CharField('название статьи', max_length = 200) #поля для ввода текста(хранение небольшого текста), image , file, publishing date (база-данных)
    blog_text = models.TextField("текст статьи")# хранение большого текста
    published_date = models.DateTimeField('дата публикации')


    def __str__(self):
        return self.blog_titles


    def was_published_recently(self): #если публикация была выпущена за в течении 7 дней(была ли статья опупликована недавно! )
        return self.published_date >= (timezone.now() - datetime.timedelta(days = 7))



    class Meta:
        verbose_name = 'Статья' # название данной модели в ед числе
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    blog = models.ForeignKey(Article, on_delete = models.CASCADE )#будет привязываться то что на верху, каскад когда удалим статью удалится все написанные на него тоже
    author_name = models.CharField('имя автора',max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий' # название данной модели в ед числе
        verbose_name_plural = 'Комментарии'