from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

CRM_ADMIN = 'crm-admin'
MANAGER = 'manager'
USER = 'user'


class UserManager(BaseUserManager):
    """Кастомный менеджер для User."""

    def create_user(self, username,  password=None):
        """Создает пользователя.

        Args:
            username (str): имя пользователя
            password (int, optional): пароль. По умолчанию - None.

        Returns:
            User: обьект пользователя.
        """
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password=None):
        """Создает суперпользователя.

        Args:
            username (str): имя пользователя
            password (int, optional): пароль. По умолчанию - None.

        Returns:
            User: обьект пользователя.
        """

        user = self.create_user(
            username,
            password=password,
        )
        user.role = MANAGER
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Модель для пользователя.

    Attributes:
        role (str): роль пользователя.
        offer (bool): есть ли коммерческое предложение.
        avatar (str): аватар.
    """

    ROLES = (CRM_ADMIN, 'CRM-Admin'), (MANAGER, 'Manager'), (USER, 'User')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,)
    role = models.CharField(
        verbose_name='Роль',
        max_length=max([len(role[0]) for role in ROLES]),
        choices=ROLES,
        default='user'
    )
    offer = models.BooleanField('Коммерческое предложение', default=False)
    avatar = models.ImageField(
        'Аватар', upload_to=settings.MEDIA_ROOT.joinpath('avatars')
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        """Строковое представление модели."""

        return self.username

    def has_perm(self, perm, obj=None):
        """Проверяет есть ли у пользователя определенное разрешение."""

        return True

    def has_module_perms(self, app_label):
        """Проверяет есть ли у пользователя разрешения на просмотр 
        приложения."""

        return True

    @property
    def is_staff(self):
        """Проверяет является ли пользователь администратором."""

        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
