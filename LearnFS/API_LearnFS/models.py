from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=4, verbose_name="Класс")
    
    def __str__(self):
        return self.group
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        
class Subject(models.Model):
    subject = models.CharField(max_length=20, verbose_name="Предмет")
    
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        
class Article(models.Model):
    group = models.ForeignKey("Group", verbose_name="Класс", on_delete=models.PROTECT)
    subject = models.ForeignKey("Subject", verbose_name="Предмет", on_delete=models.PROTECT)
    title = models.CharField(max_length=127, verbose_name="Заголовок")
    summary = models.TextField(max_length=500, verbose_name="Описание")
    html = CKEditor5Field(verbose_name="HTML", config_name='extends')
    num_questions = models.CharField(verbose_name="Количество вопросов в тесте", max_length=2)
    #TODO добавить подержку фото в статье
    time_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    time_edit = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Questions(models.Model):
    article = models.ForeignKey("Article", verbose_name="Статья", on_delete=models.PROTECT)
    body = models.TextField(verbose_name="Вопрос")
    
    def __str__(self):
        return str(self.body)
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        
class Answer(models.Model):
    questions = models.ForeignKey("Questions", verbose_name="Вопрос", on_delete=models.PROTECT)
    body = models.TextField(verbose_name="Вариант ответа")
    isRight = models.BooleanField(verbose_name="Правильность")
    
    def __str__(self):
        return str(self.body)
    
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'