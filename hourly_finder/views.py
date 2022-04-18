from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([])
def getRoutes(request):
    routes = [
        {
            'Application' : 'HourlyFinder API',
            'Feature List' : [
                {
                    "Name" : "Auth",
                    "Endpoints" : [
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
                        
                    ]
                }, 
                {
                    "Name" : "Job",
                    "Endpoints" : [
                        {
                            'Endpoint': '/jobs',
                            'method': 'GET',
                            'body': None,
                            'description': 'returns job information'
                        },
                    ]
                },
                {
                    "Name" : "Blog",
                    "Endpoints" : [
                        {
                            'Endpoint': '/blogs/?page_size=6',
                            'method': 'GET',
                            'body': None,
                            'description': 'returns Blog information with pagination.'
                        },
                        {
                            'Endpoint': '/blogs/{SlugId}',
                            'method': 'GET',
                            'body': None,
                            'description': 'returns Single Blog Details information with pagination.'
                        },
                    ]
                },
                {
                    "Name" : "Contact",
                    "Endpoints" : [
                        {
                            'Endpoint': '/contact/create',
                            'method': 'POST',
                            'body': '{data}',
                            'description': 'create a query from user and send mail to HourlyFinder Team.'
                        },
                        {
                            'Endpoint': '/contact/newsletter',
                            'method': 'POST',
                            'body': '{email}',
                            'description': 'Add Newsletter Subscription via Email and get confirmation mail.'
                        }
                    ]
                }
            ]
        }
    ]
    return Response(routes)
