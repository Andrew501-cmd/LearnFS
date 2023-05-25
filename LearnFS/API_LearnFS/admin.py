from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "group", "title", "summary", "html", "num_questions", "time_create", "time_edit"]
    list_display_links = ["id", "group", "title", "summary", "html", "num_questions", "time_create", "time_edit"]

class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "group"]
    list_display_links = ["id", "group"]
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "subject"]
    list_display_links = ["id", "subject"]
    
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "article", "body"]
    list_display_links = ["id", "article", "body"]
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "questions", "body", "isRight"]
    list_display_links = ["id", "questions", "body", "isRight"]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)