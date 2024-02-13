from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length=20 , null=True , blank=True)
    otp = models.IntegerField(default=0)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()
    
    def get_username(self):
        return self.email



class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True






# Event Management System with Integrated User Authentication
# Overview
# Develop an event management system where users can register, log in, 
# and manage their participation in various events. This platform highlights the
# integration of Django's user authentication system with an application that handles event registrations and user interactions.
# Key Features
# User Registration and Login:
# Utilize Django’s built-in authentication system for user registration and login.
# Implement forms for new user registration and existing user login.
# Profile Management:
# Enable users to view and edit their profile, including personal information and preferences.
# Implement features for password change and reset.
# Event Registration and Management:
# Allow authenticated users to register for events.
# Provide a feature for users to view and manage their event registrations.
# User Dashboard:
# Create a personalized dashboard for each user.
# Include functionalities such as viewing upcoming events, past event participations, and managing account settings.
# Event Listings and Details:
# Display a list of upcoming events on the platform.
# Provide detailed information about each event, including date, time, location, and description.
# Administrator Features:
# Allow admins to create, edit, and delete events.
# Enable admin to manage user accounts and view statistics about event registrations.
# Responsive Design:
# Ensure the application is responsive and accessible on various devices.