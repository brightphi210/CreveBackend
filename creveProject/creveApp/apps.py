from django.apps import AppConfig


class CreveappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creveApp'

    def ready(self):
        import creveApp.signals