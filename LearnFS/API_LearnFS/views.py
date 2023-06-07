from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from rest_framework.views import *
from rest_framework.response import Response
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
        return Response(infoGnS())
            