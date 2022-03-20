from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

"""
AppUserMaager is inherting BaseUserManager Class to manage CustomUser fields
"""
class AppUserManager(BaseUserManager):

    def create_superuser(self, email, password=None):
        u = self.create_user(email,
                        password=password
                    )
        u.is_admin = "admin"
        u.user_type = "admin"
        u.save(using=self._db)
        return u
    
    def create_user(self, email, password=None, **extea_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extea_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

""""
custom user class with additional fields
"""
class AppUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_type


"""
Blood request model which is created to hold data for blood doner and accepter
"""
class BloodRequest(models.Model):
    blood_requested_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="acceptor")
    blood_requested_to = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="doner")
    requested_at = models.DateTimeField(auto_now_add=True)

"""
RequestToBloodBankModel is a model to get request from blood acceptor
"""
class RequestToBloodBankModel(models.Model):
    secret_key = models.CharField(null=False, blank=False, max_length=100)
    requested_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    requested_group = models.CharField(null=False, blank=False, max_length=20)