from django.conf import settings
from django.core.management.base import BaseCommand

from user_selection.models import User, CRM_ADMIN, MANAGER, USER

USERS = {
    CRM_ADMIN: settings.STATIC_ROOT.joinpath(
        'default_avatars'
    ).joinpath('crm_admin.png'),
    MANAGER: settings.STATIC_ROOT.joinpath(
        'default_avatars'
    ).joinpath('admin.png'),
    USER: settings.STATIC_ROOT.joinpath(
        'default_avatars'
    ).joinpath('user.png'),
}


class Command(BaseCommand):
    """Команда для создания пользователей, по одному на каждую роль."""

    help = 'Создает User, Manager и CRM-admin с аватарами по умолчанию'

    def handle(self, *args, **options):
        """Создает обычного пользователя, админа и crm-админа с
        дефолтными аватарами.
        """

        User.objects.bulk_create(
            User(
                username=role,
                avatar=str(avatar),
                role=role,
                is_admin=True if (
                    role == CRM_ADMIN or role == MANAGER
                ) else False,
            ) for role, avatar in USERS.items()
        )
