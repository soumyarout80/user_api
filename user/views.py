from django.shortcuts import get_object_or_404

from rest_framework import (
    status,
    viewsets
)

from rest_framework.response import Response

from .models import (
    Account,
    AccountDetail,
    Manager,
)
from .serializers import (
    AccountSerializer,
    AccountDetailsSerializer,
    ManagerSerializer,
)


class AccountViewSet(viewsets.ViewSet):
    def list(self, request):
        resources = Account.objects.all()
        serializer = AccountSerializer(resources, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class AccountDetailViewSet(viewsets.ViewSet):
    def list(self, request):
        resources = AccountDetail.objects.all()
        serializer = AccountDetailsSerializer(resources, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AccountDetail.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AccountDetailsSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = AccountDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ManagerViewSet(viewsets.ViewSet):
    def list(self, request):
        resources = Manager.objects.all()
        serializer = ManagerSerializer(resources, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Manager.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ManagerSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = ManagerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass