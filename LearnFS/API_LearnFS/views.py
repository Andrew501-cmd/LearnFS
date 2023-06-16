from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Group, Subject
from rest_framework.views import *
from rest_framework.response import Response
import urllib.parse
from django.core.exceptions import *
# Create your views here.

def documentation(request):
    return HttpResponse('v1/allList</br>')

"""def V1_allList(request):
    article = Article.objects.all()
    gns = []
    for i in range(len(article)):
        pk = i + 1
        group = Article.objects.get(pk=pk).group
        subject = Article.objects.get(pk=pk).subject
        gns_mesne = str(group), str(subject)
        print(gns_mesne)
        if gns_mesne not in gns:
            gns.append(gns_mesne)
    
    return HttpResponse(gns)"""
    
class V1_allList(APIView):
    def get(self, request):
        def infoGnS(): #Возвращает информацию о классах и придметах
            try:
                body_groups = []
                body_subjects = [] 
                ListGroupAndSubject = {}
                for i in range(len(Article.objects.all())):
                    pk = i + 1
                    group = str(Article.objects.get(pk=pk).group)
                    subject = str(Article.objects.get(pk=pk).subject)
                    if group not in body_groups:
                        body_groups.append(group)
                    if subject not in body_subjects:
                        body_subjects.append(subject)
                quantity_groups = len(body_groups)
                quantity_subjects = len(body_subjects)
                for i in body_groups:
                    subject = list(Article.objects.filter(group=i))
                    subject_filter = list()
                    for x in range(len(subject)):
                        if str(subject[x]) not in subject_filter:
                            subject_filter.append(str(subject[x]))
                    ListGroupAndSubject[i] = subject_filter
                    
                return {'group': {"quantity": quantity_groups, "body_groups": body_groups},
                            "subject": {"quantity": quantity_subjects, "body_groups": body_subjects},
                            "ListGroupAndSubject": ListGroupAndSubject}
            except Exception as exp:
                return Response({"request": request, "response": {"error": {"exception": str(exp), "comment": "Если вы не знаете с чем связана ошибка, обратитесь к администратору", "headers": request.headers}}})
        return Response(infoGnS())
        
class V2_allList(APIView):
    def get(self, request): 
        def infoGnS(): #Возвращает информацию о классах и придметах
            body_groups = []
            body_subjects = [] 
            ListGroupAndSubject = []
            for i in range(len(Article.objects.all())):
                pk = i + 1
                group = str(Article.objects.get(pk=pk).group)
                subject = str(Article.objects.get(pk=pk).subject)
                GnS = group + " " + subject
                if GnS not in ListGroupAndSubject:
                    ListGroupAndSubject.append(GnS)
                if group not in body_groups:
                    body_groups.append(group)
                if subject not in body_subjects:
                    body_subjects.append(subject)
            quantity_groups = len(body_groups)
            quantity_subjects = len(body_subjects)
            return {'group': {"quantity": quantity_groups, "body_groups": body_groups},
                           "subject": {"quantity": quantity_subjects, "body_groups": body_subjects},
                           "ListGroupAndSubject": ListGroupAndSubject}
        return Response(infoGnS())
    
class getArticle(APIView):
    def get(self, request):
        id = request.GET.get("id")
        subject = request.GET.get("sub")
        group = request.GET.get("group")
        try:
            if id != None and subject == None and group == None:
                    if not id.isnumeric():
                        return Response({"request": {"id": id}, "response": {"error": "Поле ID должно быть int", "headers": request.headers}})
                    res = Article.objects.get(pk=id)
                    return Response({"request": {"id": id}, "response": {"id": str(res.pk), "group": str(res.group), "subject": str(res.subject), "title": str(res.title), "summary": str(res.summary), "html": str(res.html), "num_questions": str(res.num_questions), "time_create": str(res.time_create), "time_edit": str(res.time_edit)}})
            if id == None and subject != None and group != None:
                resp = []
                id_sub = Subject.objects.get(subject=subject).pk
                id_group = Group.objects.get(group=group).pk
                article = Article.objects.filter(subject=id_sub, group=id_group)
                for i in range(len(article)):
                    art = article[i]
                    resp.append({"id": str(art.pk), "group": str(art.group), "subject": str(art.subject), "title": str(art.title), "summary": str(art.summary), "html": str(art.html), "num_questions": str(art.num_questions), "time_create": str(art.time_create), "time_edit": str(art.time_edit)})
                return Response({"request": {"sub": subject, "group": group}, "response": resp})
            else:
                return Response({"request": {"id": id,"sub": subject, "group": group}, "response": {"error": {"exception": "Не правильно указаны параметры в запросе", "comment": "Если вы не знаете с чем связана ошибка, обратитесь к администратору", "headers": request.headers}}})
        except Exception as exp:
            return Response({"request": {"id": id,"sub": subject, "group": group}, "response": {"error": {"exception": str(exp), "comment": "Если вы не знаете с чем связана ошибка, обратитесь к администратору", "headers": request.headers}}})
            
class searchArticle(APIView):
    def get(self, request):
        return Response("Метод находится в разроботке")