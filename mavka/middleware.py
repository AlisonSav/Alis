from datetime import datetime

from django.urls import reverse

from .models import LogModel


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        created_at = datetime.utcnow()
        response = self.get_response(request)
        if not request.path.startswith(reverse("admin:index")):
            print(
                f"Path - {request.path}, method - {request.method}, body - {request.POST}, "
                f"query - {request.GET}, request - {request.__dict__}"
            )
            print(f"Request at - {created_at}")
            LogModel.objects.create(path=request.path, method=request.method, created_at=created_at, data=request.POST)
        return response
