from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Autentica um usuário Django e retorna um token para usar na API.
    
    Requisição esperada:
    POST /api/login/
    {
        "username": "usuario",
        "password": "senha123"
    }
    
    Resposta:
    {
        "token": "abc123...",
        "user_id": 1,
        "username": "usuario"
    }
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'detail': 'Username e password são obrigatórios'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Usar a função authenticate do Django
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response(
            {'detail': 'Username ou password incorretos'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Criar ou obter token Django
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user_id': user.id,
        'username': user.username
    }, status=status.HTTP_200_OK)