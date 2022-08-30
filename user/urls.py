from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AccountViewSet,
    AccountDetailViewSet,
    ManagerViewSet,
)

urlpatterns = [
    path('v1/', AccountViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('v1/<int:pk>/', AccountViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
    path('details/v1/', AccountDetailViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('details/v1/<int:pk>/', AccountDetailViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
    path('manager/v1/', ManagerViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('manager/v1/<int:pk>/', ManagerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
]
