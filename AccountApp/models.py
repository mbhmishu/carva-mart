from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class AppUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text= gettext_lazy('Designates whether the user can be staff or login this site')   
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text= gettext_lazy('Designates whether this user should be treated as active. unselect this instead of deleting account ')
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class User_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    username = models.CharField(max_length=264, blank=True, null=True)
    full_name = models.CharField(max_length=264, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value= getattr(self,field_name)
            if value is None or value=='':
                return False
        return True




@receiver(post_save, sender=User)
def create_profile(sender, instance,created, **kwargs):
    if created:
        User_info.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance,**kwargs):
    instance.user_info.save()
