from django.shortcuts import render
from django.http import HttpResponse

def dos(request):
    a="""
<h1>Rama2 </h1> 
<h3>Completado</h3>
"""
    return HttpResponse(a)