from django.db.models import Manager

class CustomManager(Manager):
    def get_queryset(self):
        return super().get_queryset().all().order_by('name')

