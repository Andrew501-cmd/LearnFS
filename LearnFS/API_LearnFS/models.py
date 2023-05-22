from django.db import models

# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=5)
    
    def __str__(self):           
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=35)
    groups = models.ManyToManyField(Group)
    
    def __str__(self):          
        return self.name
    
class Theme(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    subs_clases = models.ForeignKey('Subject', on_delete=models.PROTECT)
    
    def __str__(self):          
        return self.name
    
class Summary(models.Model):
    body = models.TextField()
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    themes = models.ForeignKey("Theme",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.TextField()
    tests = models.ForeignKey("Test",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Ans_Que(models.Model):
    answer = models.CharField(max_length=255)
    isRight = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name