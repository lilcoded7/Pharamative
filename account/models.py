from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models 
import random



class MyAccountManager(BaseUserManager):
    def create_superuser(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have a username.")
        if not email:
            raise ValueError("Users must have an email address.")
        if "@" not in email and ".com" not in email:
            raise ValueError("Invalid email input")
        if len(password) < 8:
            raise ValueError("Password 8 must contain at least 8 characters")

        user = self.model(username=username, email=self.normalize_email(email))
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_verified = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if "@" not in email and ".com" not in email:
            raise ValueError("Invalid email input")
        if len(password) < 8:
            raise ValueError("Password 8must contain at least 8 characters")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username    = models.CharField(max_length=100, unique=True)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=20)
    address     = models.CharField(max_length=100, null=True, blank=True)
    verify_code = models.CharField(max_length=100)
    ref_code    = models.CharField(max_length=6, null=True, blank=True)
    last_login  = models.DateTimeField(auto_now_add=True)

    is_vip = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_verified  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['-id'] 

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        num = random.randint(00000, 99990)
        self.verify_code = num 

        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



