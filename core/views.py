from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):

    saudacao = ('<h1>Hello {} de {} anos!</h1>.'.format(nome, idade))
    return HttpResponse(saudacao)

def soma(request, a, b):
    soma = a + b
    return HttpResponse('Soma = {}'.format(soma))