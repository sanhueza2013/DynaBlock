from django.apps import AppConfig


class TimeManagementConfig(AppConfig):
    name = 'time_management'

    def ready(self):
        import time_management.signals  # noqa
