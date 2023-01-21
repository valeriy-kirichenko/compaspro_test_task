from django.conf import settings
from django.core.management.base import BaseCommand

from user_selection.models import User, CRM_ADMIN, MANAGER, USER

USERS = {
    CRM_ADMIN: settings.STATICFILES_DIRS[0].joinpath(
        'default_avatars'
    ).joinpath('crm_admin.png'),
    MANAGER: settings.STATICFILES_DIRS[0].joinpath(
        'default_avatars'
    ).joinpath('admin.png'),
    USER: settings.STATICFILES_DIRS[0].joinpath(
        'default_avatars'
    ).joinpath('user.png'),
}


class Command(BaseCommand):
    help = 'Create User, Manager and CRM-admin with default avatars'

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
