from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    return HttpResponse("""
                        <h1>Rama 1</h1>
                        <br>
                        <h2>Creada</h2>
                        """)