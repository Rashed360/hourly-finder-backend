# Hourly Finder Backend using Django REST API

### API Endpoints

```json
[
    {
        "Application": "HourlyFinder API",
        "Feature List": [
            {
                "Name": "Auth",
                "Endpoints": [
                    {
                        "Endpoint": "/auth",
                        "method": "GET",
                        "body": null,
                        "description": "returns authentication"
                    },
                    {
                        "Endpoint": "/user",
                        "method": "GET",
                        "body": null,
                        "description": "returns user information"
                    }
                ]
            },
            {
                "Name": "Job",
                "Endpoints": [
                    {
                        "Endpoint": "/jobs",
                        "method": "GET",
                        "body": null,
                        "description": "returns job information"
                    }
                ]
            },
            {
                "Name": "Blog",
                "Endpoints": [
                    {
                        "Endpoint": "/blogs/?page_size=6",
                        "method": "GET",
                        "body": null,
                        "description": "returns Blog information with pagination."
                    },
                    {
                        "Endpoint": "/blogs/{SlugId}",
                        "method": "GET",
                        "body": null,
                        "description": "returns Single Blog Details information with pagination."
                    }
                ]
            },
            {
                "Name": "Contact",
                "Endpoints": [
                    {
                        "Endpoint": "/contact/create",
                        "method": "POST",
                        "body": "{data}",
                        "description": "create a query from user and send mail to HourlyFinder Team."
                    },
                    {
                        "Endpoint": "/contact/newsletter",
                        "method": "POST",
                        "body": "{email}",
                        "description": "Add Newsletter Subscription via Email and get confirmation mail."
                    }
                ]
            }
        ]
    }
]
```

### Requirements

```json
asgiref==3.5.0
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.12
coreapi==2.3.3
coreschema==0.0.4
cryptography==36.0.1
defusedxml==0.7.1
Django==4.0.2
django-cors-headers==3.11.0
django-templated-mail==1.1.1
djangorestframework==3.13.1
djangorestframework-simplejwt==4.8.0
djoser==2.1.0
gunicorn==20.1.0
idna==3.3
itypes==1.2.0
Jinja2==3.0.3
MarkupSafe==2.1.0
oauthlib==3.2.0
Pillow==9.0.1
pycparser==2.21
PyJWT==2.3.0
python-decouple==3.6
python3-openid==3.2.0
pytz==2021.3
requests==2.27.1
requests-oauthlib==1.3.1
six==1.16.0
social-auth-app-django==4.0.0
social-auth-core==4.2.0
sqlparse==0.4.2
tzdata==2021.5
uritemplate==4.1.1
urllib3==1.26.8
whitenoise==6.0.0
```