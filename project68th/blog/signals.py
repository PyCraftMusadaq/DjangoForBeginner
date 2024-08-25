from django.dispatch import Signal, receiver
notifications = Signal()


@receiver(notifications)
def show_notification(sender,**kwargs):
    print("---------------------")
    print("sender:",sender)
    print(f"Kwargs: {kwargs}")