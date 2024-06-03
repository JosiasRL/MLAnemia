from django.apps import AppConfig


class AppmlConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "AppML"
    verbose_name = "perfiles"
    
    def ready(self) -> None:
        import AppML.signals
