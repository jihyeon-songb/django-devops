from django.urls import path,include
from rest_framework.routers import DefaultRouter
from task.views import *

router = DefaultRouter()
router.register(r'todo',TodoModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
