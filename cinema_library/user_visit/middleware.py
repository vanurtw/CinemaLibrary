import django.db.transaction
from django.utils import timezone
from .models import UserVisit


@django.db.transaction.atomic
def save_user_visit(user_visit):
    try:
        user_visit.save()
    except:
        pass


class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            return self.get_response(request)
        if 'admin' in request.META.get('HTTP_REFERER', ''):
            return self.get_response(request)

        uv = UserVisit.objects.build(request, timezone.now())
        save_user_visit(uv)
        return self.get_response(request)
