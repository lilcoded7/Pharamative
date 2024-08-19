from django.apps import AppConfig


class CaffoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CAFFOOD'

    def ready(self):
        import CAFFOOD.signals