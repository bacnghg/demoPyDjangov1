from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    myname = "Bacws Nguyen"
    programLanguage = ["Python", "Golang", "Ruby", "JS"]
    context = {"name": myname, "mySkill": programLanguage}
    return render(request, "polls/index.html", context)

def getUser(request):
    return HttpResponse("<h1>Get all User vote</h1>")

def viewList(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}

    return render(request, "polls/question_list.html", context)