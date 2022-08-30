from django.db import models
import yaml
import datetime


def read_country_from_yaml_file():
    countries = list()
    with open('user/countries.yml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

        for country_code, country in fruits_list['countries'].items():
            temp = (country, country)
            countries.append(temp)
    return countries


def read_states_from_yaml_file():
    states = list()
    with open('user/states.yml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

        for state_code, state in fruits_list['states'].items():
            temp = (state_code, state)
            states.append(temp)
    return states


STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Pending', 'Pending'),
    ('Under Review', 'Under Review'),
)

GENDER__CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Agender', 'Agender'),
    ('Non-binary', 'Non-binary'),
    ('Bigender', 'Bigender'),
    ('Polygender', 'Polygender'),
    ('Genderqueer', 'Genderqueer'),
    ('Genderfluid', 'Genderfluid'),
)


class Account(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(
        max_length=100,
        unique=True
    )
    phone = models.CharField(
        max_length=15,
        unique=True
    )
    password = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=11,
        choices=GENDER__CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(days=30)
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '{}: {}_{}'.format(self.id, self.first_name, self.last_name)


class AccountDetail(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=128)
    description = models.TextField()
    state = models.CharField(
        max_length=40,
        default="Karnataka",
        null=True
    )
    country = models.CharField(
        max_length=50,
        choices=read_country_from_yaml_file(),
        null=True
    )
    zip_code = models.CharField(max_length=20, default=560103)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    def __str__(self):
        return '{} ( {} )'.format(self.account, self.title)

    class Meta:
        ordering = ['title']


class Manager(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True
    )
    manager_name = models.CharField(max_length=64)
    manager_email = models.CharField(max_length=100, null=True)
    manager_phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return "%s the manager of %s" % (self.manager_name, self.account)
