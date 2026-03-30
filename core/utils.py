from django.conf import settings


def user_can_edit(user):
    if not user.is_authenticated:
        return False
    return user.email in settings.ALLOWED_EDITOR_EMAILS