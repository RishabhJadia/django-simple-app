from django.apps import AppConfig


class DeniAppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deni_apps'

    # def ready(self):
    #     from scheduler import updater
    #     updater.start()