from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('movie', views.MovieViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('category-all/', views.CategoreAPIView.as_view()),

]
