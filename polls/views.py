from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    myname = "Bacws Nguyen"
    programLanguage = ["Python", "Golang", "Ruby", "JS"]
    context = {"name": myname, "mySkill": programLanguage}
    return render(request, "polls/index.html", context)

def getUser(request):
    return HttpResponse("<h1>Get all User vote</h1>")