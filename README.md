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
