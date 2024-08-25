from django.db.models import Manager

class CustomManager(Manager):
    def get_stu_roll(self,r1,r2):
        return super().get_queryset().filter(roll__range=(r1,r2))
    

