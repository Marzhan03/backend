from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, first_name=None, last_name=None, phone_number=None, date_of_birth=None, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField("Логин пользователя", max_length=255, unique=True,null=True)

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
     null = True,
    )

    date_of_birth = models.DateField(null=True)

    first_name = models.CharField("Имя пользователя", max_length=255,null=True)

    last_name = models.CharField("Фамилия пользователя", max_length=255,null=True)

    phone_number = models.CharField("Телефон", max_length=255,null=True)

    is_active = models.BooleanField(default=True,null=True)

    is_admin = models.BooleanField(default=False,null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin