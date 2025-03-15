from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from .models import User
from .serializers import userSerializer

import json

@api_view(['GET'])
def  get_users(request):

    if request.method == 'GET': # verifica se o método é GET

        users = User.objects.all() # obtém todos os usuários da classe User

        serializer = userSerializer(users, many=True) # serializa os usuários em JSON (atributo many retorna vários, não é objeto único)

        return Response(serializer.data) # retorna a resposta do serializer
    
    return Response(status=status.HTTP_400_BAD_REQUEST) # retorna o status 404 se não passar no IF


@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = userSerializer(user) # objeto único

        return Response(serializer.data)