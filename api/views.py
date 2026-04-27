from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
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


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def upload_image(request):
    """
    Faz upload de uma imagem e retorna o caminho da imagem.
    
    Requisição esperada:
    POST /api/upload/image/
    Content-Type: multipart/form-data
    Arquivo: [arquivo de imagem]
    
    Resposta:
    {
        "image_url": "/media/images/filename.jpg"
    }
    """
    if 'image' not in request.FILES:
        return Response(
            {'detail': 'Campo "image" é obrigatório'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    image_file = request.FILES['image']
    
    # Validar tipo de arquivo
    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
    file_extension = image_file.name.split('.')[-1].lower()
    
    if file_extension not in allowed_extensions:
        return Response(
            {'detail': f'Tipo de arquivo não permitido. Use: {", ".join(allowed_extensions)}'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validar tamanho (máx 5MB)
    if image_file.size > 5 * 1024 * 1024:
        return Response(
            {'detail': 'Arquivo muito grande. Máximo 5MB'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Salvar o arquivo em media/images/
    from django.core.files.storage import default_storage
    from django.utils import timezone
    import uuid
    
    # Gerar nome único para o arquivo
    file_name = f"images/{uuid.uuid4()}_{image_file.name}"
    
    # Salvar o arquivo
    file_path = default_storage.save(file_name, image_file)
    
    return Response({
        'image_url': f'/media/{file_path}',
        'filename': file_path
    }, status=status.HTTP_201_CREATED)