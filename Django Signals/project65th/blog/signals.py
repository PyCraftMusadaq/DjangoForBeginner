from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User 
from django.db.models.signals import pre_init, post_init, pre_delete, post_delete, pre_save, post_save, pre_migrate, post_migrate 
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created
from django.dispatch import receiver


# connecting using decorator 
# functions 
@receiver(user_logged_in, sender=User)
def login_success(sender,request,user,**kwargs):
    print("-----------------------------")
    print("Loged-in Signal")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print("Username:",user.username)
    print("password:",user.password)
    print(f"Kwargs: {kwargs}")


# connecting using method 
#user_logged_in.connect(login_success,sender=User)
@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("--------------------")
    print("Loged-out Signal")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print("username",user.username)
    print(f"Kwargs: {kwargs}")
#user_logged_out.connect(logout_sucess sender=User)

# user login failed 
@receiver(user_login_failed)
def login_failed(sender,credentials,request, **kwargs):
    print("Sorry Login Failed :( ")
    print("Credentials: ",credentials)

# user_login_failed.connect(user_login_failed)



# models related signals 
@receiver(pre_save, sender=User)
def at_beginning_save(sender,instance, **kwargs):
    print("--------------------")
    print("Pre-Save Signal")
    print("Model Signal")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f"Kwargs: {kwargs}")

#pre_save.coonect(at_beginning_save, sender=User)



@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("---------------------")
        print("Post Save Signal")
        print("New Record Created")
        print("created at: ", created)
        print("Sender",sender)
        print("Instance",instance)
        print(f"Kwargs {kwargs}")
    else:
        print("---------------------")
        print("Post Save Signal")
        print("Record Updated")
        print("Sender",sender)
        print("Instance",instance)
        print(f"Kwargs {kwargs}")

#post_save.connect(at_ending_save, sender=User)

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("--------------------------------")
    print("Pre Delete Signal")
    print("Sender ",sender)
    print("instance ", instance)
    print(f"kwargs: {kwargs}")

# pre_delete(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-----------------------------")
    print("Post Delete Signal ")
    print("instance: ", instance)
    print("Sender: ", sender)
    print(f"Kwargs: {kwargs}")


# init method 
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("-----------------------------")
    print("Pre Init Signal ")
    print("Sender: ", sender)
    print(f"Args: {args}")
    print(f"Kwrgs: {kwargs}")

# pre_init.connect(at_beginning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("--------------------------")
    print("Post Init Signal ")
    print("sender: ", sender)
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")



# request related 
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("--------------------------------")
    print(" Request Started signal ")
    print("Sender:", sender)
    print("Environ: ", environ)
    print(f"Kwargs: {kwargs}")

# request_started.connect(at_beginning_reques, sender=User)


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("--------------------------------")
    print(" Request Started signal ")
    print("Sender:", sender)
    print(f"Kwargs: {kwargs}")

# request_started.connect(at_ending_reques, sender=User)

@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("-----------------------------")
    print("At Request Exception")
    print("Sender: ", sender)
    print("Request: ", request)
    print(f"Kwargs: {kwargs}")

# got_request_exception.connect(at_req_exception, sender=User)


# Migrate related Signals 
@receiver(pre_migrate, sender=User)
def before_install_app(sender,app_config,verbosity, interactive,using,plan,apps,**kwargs):
    print("------------------------------------")
    print("Before Instll Apps")
    print("Sender: ", sender)
    print("App config: ",app_config)
    print("Verbosity: ", verbosity)
    print("interactive: ", interactive)
    print("Using: ", using)
    print("Plan ", plan)
    print("Apps: ",apps)
    print(f" Kwargs: {kwargs}")

# pre_migrate.connect( before_install_app, sender=User)

@receiver(post_migrate, sender=User)
def at_end_migrate_flush(sender,app_config,verbosity, interactive,using,plan,apps,**kwargs):
    print("------------------------------------")
    print("After Install Apps")
    print("Sender: ", sender)
    print("App config: ",app_config)
    print("Verbosity: ", verbosity)
    print("interactive: ", interactive)
    print("Using: ", using)
    print("Plan ", plan)
    print("Apps: ",apps)
    print(f" Kwargs: {kwargs}")
    
# post_migrate.connect(at_end_migrate_flush, sender=User)


# Database related signals 
@receiver(connection_created)
def conn_db(sender, connection,**kwargs):
    print("------------------------")
    print("Initial connection to the database ")
    print("Sender:", sender)
    print("Connection: ", connection )
    print(f"Kwargs: {kwargs}")

#connection_created.connect(conn_db)