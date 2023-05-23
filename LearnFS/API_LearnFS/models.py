from django.db import models

# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=5)
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
    
    def __str__(self):           
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=35)
    groups = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
    
    def __str__(self):          
        return self.name
    
class Theme(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    subs_clases = models.ForeignKey('Subject', on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
    
    def __str__(self):          
        return self.name
    
class Summary(models.Model):
    body = models.TextField()
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'
    
    def __str__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.TextField()
    tests = models.ForeignKey("Test",on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.name
    
class Ans_Que(models.Model):
    answer = models.CharField(max_length=255)
    isRight = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'
    
    def __str__(self):
        return self.name