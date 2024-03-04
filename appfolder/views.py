from django.shortcuts import render


# Create your views here.
from appfolder.models import *


def index(request):
    servis = Service.objects.all()
    portfolio = Portfolio.objects.all()
    team = Team.objects.all()
    return render(request,'index.html',{"servis":servis,"portfolio":portfolio,"team":team})
def portfolio(ppp):
    return render(ppp,'portfolio-details.html')
