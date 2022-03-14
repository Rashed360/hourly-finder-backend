from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
@permission_classes([])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/auth',
            'method': 'GET',
            'body': None,
            'description': 'returns authentication'
        },
        {
            'Endpoint': '/user',
            'method': 'GET',
            'body': None,
            'description': 'returns user information'
        },
        {
            'Endpoint': '/jobs',
            'method': 'GET',
            'body': None,
            'description': 'returns job information'
        },
    ]
    return Response(routes)