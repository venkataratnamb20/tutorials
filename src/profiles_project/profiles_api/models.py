from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django  work with our custom user model"""
    def create_user(self, email, firstname, lastname, password=None):
        """Create new user profile object"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname)

        user.set_password = password       # Encrypts the password.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, firstname, lastname, password):
        """Create new super user for a given details"""
        user = self.create_user(email, firstname, lastname, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PendingDeprecationWarning):
    """User profile in the system"""
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']

    def get_full_name(self):
        """Used to get the user full name"""
        return self.firstname + ' ' + self.lastname

    def get_short_name(self):
        """Used to get User short name"""
        return self.firstname

    def __str__(self):
        """Django uses this when it needs to convert an object to a string"""
        return self.email

