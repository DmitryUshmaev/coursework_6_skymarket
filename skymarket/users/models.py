from random import choices

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserRoles, UserManager


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=3, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='avatars', null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER
