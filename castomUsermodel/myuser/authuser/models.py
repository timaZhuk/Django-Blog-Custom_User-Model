from typing import Any
from django.db import models
# import this model for DB
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
from django.utils import timezone

# Create your models here.
#create a model for User
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        #--built-in django function
        email = self.normalize_email(email)
        # creating user model
        user = self.model(email=email, **extra_fields)
        # set password field
        user.set_password(password)
        user.save(using=self._db)

        return user
    #for  user (not regular user)
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, **extra_fields)
    
    #for creating superuser
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, **extra_fields) 
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='',unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    # date when user joint
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CustomUserManager()
    #define fildes in form
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural='Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    

    

                    
                     


