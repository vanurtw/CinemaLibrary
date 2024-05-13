from django.contrib.auth import get_user_model
from django.db import models
import user_agents
from django.utils import timezone
import hashlib
import uuid


# Create your models here.

def parse_remote_addr(request):
    x_forwared_for = request.headers.get('X-Forwarded-For', '')
    if x_forwared_for:
        return x_forwared_for.split(',')[0]
    return request.META.get('REMOTE_ADDR', '')


def parse_ua_string(request):
    return request.headers.get('User-Agent', '')


def parse_content_type(request):
    return request.META.get('CONTENT_TYPE')


def parse_context(request):
    if request.method == 'POST':
        context = {i: request.POST.get(i) for i in request.POST}
        return context


class UserVisitManager(models.Manager):
    def build(self, request, timestamp):
        uv = UserVisit(
            user=request.user,
            timestamp=timestamp,
            http_method=request.method,
            resource=request.build_absolute_uri(),
            session_key=request.session.session_key,
            remote_addr=parse_remote_addr(request),
            ua_string=parse_ua_string(request),
            content_type=parse_content_type(request),
            context=parse_context(request)
        )
        uv.hash = uv.md5().hexdigest()
        uv.browser = uv.user_agent.get_browser()[:200]
        uv.device = uv.user_agent.get_device()[:200]
        uv.os = uv.user_agent.get_os()[:200]
        return uv


class UserVisit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_visits')
    resource = models.CharField(max_length=255, blank=True, default='')
    http_method = models.CharField(max_length=255, blank=True, default='')
    # http_method = models.CharField()
    timestamp = models.DateTimeField(default=timezone.now)
    session_key = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, default='', blank=True)
    remote_addr = models.CharField(max_length=255, blank=True)
    ua_string = models.TextField(blank=True)
    browser = models.CharField(max_length=255, blank=True, default='')
    device = models.CharField(max_length=255, blank=True, default='')
    os = models.CharField(max_length=200, blank=True, default='')
    hash = models.CharField(max_length=255, help_text='"MD5 hash generated from request properties', unique=True)
    context = models.JSONField(default=dict, blank=True, null=True)
    objects = UserVisitManager()

    def save(self, *args, **kwargs):
        # self.hash = self.md5().hexdigest()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user} visited the site on {self.timestamp}"

    @property
    def user_agent(self):
        return user_agents.parsers.parse(self.ua_string)

    @property
    def date(self):
        return self.timestamp.date()

    def md5(self):
        h = hashlib.md5(str(self.user.id).encode())
        h.update(self.timestamp.isoformat().encode())
        h.update(self.content_type.encode())
        h.update(self.session_key.encode())
        h.update(self.remote_addr.encode())
        h.update(self.ua_string.encode())
        return h
