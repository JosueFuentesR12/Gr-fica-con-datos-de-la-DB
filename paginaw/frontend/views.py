from django.shortcuts import render
from django.http import JsonResponse
from .models import Log
from django.db.models import Max
from django.db import connection

# Create your views here.
def index(request):
    #∫maxp = Log.objects.all().aggregate(Max('points'))
    #ctx = {'maxp', maxp["points__max"]}
    return render(request, "frontend/index.html") # ,ctx

def aboutus(request):
    return render(request, "frontend/aboutus.html")


def promedioF():
    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(points) FROM frontend_log")
        resultado = cursor.fetchone()
        promedio = resultado[0] if resultado else None
    return promedio


def chart(request):
    maxp = Log.objects.all().aggregate(Max('points'))
    pointList = Log.objects.all().order_by('date')
    promedio = promedioF()
    ctx = {'maxp': maxp["points__max"], "pointList": pointList, "promedio": promedio}
    return render(request, "frontend/chart.html", ctx)

def log(request):
    latest_log = list(Log.objects.order_by('date')[:5].values())
    return JsonResponse(latest_log, safe=False)
