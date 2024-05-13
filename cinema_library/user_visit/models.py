import datetime

from django.contrib.auth import get_user_model
from django.db import models
import user_agents
from django.utils import timezone
from django.http import HttpRequest
import hashlib
import datetime
from typing import Any


# Create your models here.

def parse_remote_addr(request: HttpRequest) -> str:
    x_forwarded_for = request.headers.get('X-Forwarded-For', '')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR', '')


def parse_ua_string(request: HttpRequest) -> str:
    return request.headers.get('User-Agent', '')


def parse_content_type(request: HttpRequest) -> str:
    return request.META.get('CONTENT_TYPE')


def parse_context(request: HttpRequest) -> dict:
    if request.method == 'POST':
        context = {i: request.POST.get(i) for i in request.POST}
        return context


class UserVisitManager(models.Manager):
    def build(self, request: HttpRequest, timestamp: datetime.datetime):
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
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_visits'
    )
    resource = models.CharField(
        help_text='url address of the request resource',
        max_length=255,
        blank=True,
        default=''
    )
    http_method = models.CharField(
        help_text='request method',
        max_length=255,
        blank=True,
        default=''
    )
    timestamp = models.DateTimeField(
        help_text='The time at which the first visit of the day was recorded',
        default=timezone.now
    )
    session_key = models.CharField(
        help_text='Django session identifier',
        max_length=255
    )
    content_type = models.CharField(
        help_text='content type',
        max_length=255,
        default='',
        blank=True
    )
    remote_addr = models.CharField(
        help_text='Client IP address (from X-Forwarded-For HTTP header',
        max_length=255,
        blank=True
    )
    ua_string = models.TextField(
        help_text='Client User-Agent HTTP header',
        blank=True
    )
    browser = models.CharField(
        max_length=255,
        blank=True,
        default=''
    )
    device = models.CharField(
        help_text='device type',
        max_length=255,
        blank=True,
        default=''
    )
    os = models.CharField(
        help_text='Operating System',
        max_length=200,
        blank=True,
        default=''
    )
    hash = models.CharField(
        help_text='"MD5 hash generated from request properties',
        max_length=255,
        unique=True)
    context = models.JSONField(
        help_text='data sent in the request',
        default=dict,
        blank=True,
        null=True)
    objects = UserVisitManager()

    def save(self, *args: Any, **kwargs: Any) -> None:
        # self.hash = self.md5().hexdigest()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user} visited the site on {self.timestamp}"

    @property
    def user_agent(self) -> user_agents.parsers.UserAgent:
        return user_agents.parsers.parse(self.ua_string)

    @property
    def date(self) -> datetime.date:
        return self.timestamp.date()

    def md5(self):
        h = hashlib.md5(str(self.user.id).encode())
        h.update(self.timestamp.isoformat().encode())
        h.update(self.content_type.encode())
        h.update(self.session_key.encode())
        h.update(self.remote_addr.encode())
        h.update(self.ua_string.encode())
        return h
