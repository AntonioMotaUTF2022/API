from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from .models import User
from .serializers import userSerializer

import json

@api_view(['GET'])
def  get_all_users(request):

    if request.method == 'GET': # verifica se o método é GET

        users = User.objects.all() # obtém todos os usuários da classe User

        serializer = userSerializer(users, many=True) # serializa os usuários em JSON (atributo many retorna vários, não é objeto único)

        return Response(serializer.data) # retorna a resposta do serializer
    
    return Response(status=status.HTTP_400_BAD_REQUEST) # retorna o status 404 se não passar no IF


@api_view(['GET'])
def get_by_nick(request, nick): #recebe a request e a string nick, que vem logo depois de /user/, no url
    try:
        user = User.objects.get(pk=nick) #tenta obter o objeto User relacionado à primary key nick
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) # se não encontrat, retorna status 404
    
    if request.method == 'GET':
        
        serializer = userSerializer(user) # objeto único a ser transformado em JSON

        return Response(serializer.data, status=status.HTTP_200_OK) # retorna o JSON e o status 200
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']: # verifica se tem o parâmetro user no request
                user_nickname = request.GET['user'] # se tiver, aloca o parâmetro user na var user_nickname

                try:
                    user = User.objects.get(pk=user_nickname) # tenta encontrar o user
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND) # se não encontrar, retorna status 404
            
                serializer = userSerializer(user) # se encontrar, serializa o usuário encontrato (objeto)
                return Response(serializer.data, status=status.HTTP_200_OK) # retorna o dado e status 200
        
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) # se não tiver parâmetro user, retorna 400 bad request
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) # qualquer erro, retorna 400 bad request
        

    if request.method == 'POST':

        new_user = request.data # pega os dados recebidos no request

        serializer = userSerializer(data=new_user) # não estamos serializando um objeto, mas dados

        if serializer.is_valid(): # o serializer tem a função de verificar se os dados são válidos
            serializer.save() # se sim, salva
            return Response(status=status.HTTP_201_CREATED) # retorna o status 201 created
        
        return Response(status=status.HTTP_400_BAD_REQUEST) # se não for válido, retorna 400 bad request
    
    if request.method == 'PUT':

        nickname = request.data['user_nickname'] # pega o valor nickname enviado na request com o nome de user_nickname

        try:
            updated_user = User.objects.get(pk=nickname) # tenta achar o usuário a ser modificado
        except:
            return Response(status=status.HTTP_404_NOT_FOUND) # se não achar, retorna 404 not found

        serializer = userSerializer(updated_user, data=request.data) # colocando o objeto que vai ser editado na frente, ele substitui pelo request.data

        if serializer.is_valid():
            serializer.save() # se for válido, salva a mudança
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # e retorna o status 202, accepted
        
        return Response(status=status.HTTP_400_BAD_REQUEST) # se não for válido, retorna 400 bad request