from django.db import models

# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=5, verbose_name="Класс")
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        db_table_comment = "Таблица с классами"
        
    def __str__(self):           
        return self.group
    
class Subject(models.Model):
    name = models.CharField(max_length=35, verbose_name="Предмет")
    groups = models.ManyToManyField(Group)
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        db_table_comment = "Таблица с предметами"
        
    def __str__(self):          
        return self.name
    
class Theme(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок/название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    subs_clases = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name="Предмет")
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        db_table_comment = "Таблица с темами"
        
    def __str__(self):          
        return self.title
    
class Summary(models.Model):
    body = models.TextField(verbose_name="Конспект")
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT, verbose_name="Тема")
    
    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'
        db_table_comment = "Таблица с ответами конспектами по какой-либо теме"
        
    def __str__(self):
        return self.body

class Test(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT, verbose_name="Тема")
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        db_table_comment = "Таблица с тестами по какой-либо теме"
        
    def __str__(self):
        return self.title
    
class Question(models.Model):
    text = models.TextField(verbose_name="Вопрос")
    tests = models.ForeignKey("Test",on_delete=models.PROTECT, verbose_name="Тест")
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        db_table_comment = "Таблица с вопросами"
        
    def __str__(self):
        return self.text
    
class Ans_Que(models.Model):
    answer = models.CharField(max_length=255, verbose_name="Ответ")
    isRight = models.BooleanField(default=False, verbose_name="Правильность")
    questions = models.ForeignKey("Question",on_delete=models.PROTECT, verbose_name="Вопрос")
    
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'
        db_table_comment = "Таблица с ответами на вопросы"
    
    def __str__(self):
        return self.answer