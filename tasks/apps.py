from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from django.core.management import call_command
        try:
            call_command('migrate', interactive=False)
        except Exception:
            pass
