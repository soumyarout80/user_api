from rest_framework import serializers
from .models import (
    Account,
    AccountDetail,
    Manager
)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
