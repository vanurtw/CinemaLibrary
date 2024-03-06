from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', views.HomeViewListGeneric)

urlpatterns = [
    path('movie-all/', include(router.urls)),


]
