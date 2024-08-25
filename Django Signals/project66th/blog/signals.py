from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User 
from django.dispatch.dispatcher import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    #print("------------------------------")
    #print("Logged-in Signal.. Run Intro")
    ip = request.META.get('REMOTE_ADDR')
    #print("IP: ", ip)
    request.session['ip'] = ip