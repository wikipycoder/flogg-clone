from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# class UserType(models.Model):
#     name = models.CharField(max_length=256)

#     def __str__(self):
#         return self.name
        

class MyUserManager(BaseUserManager):
    
    def create_user(self, email,password=None):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
    
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, username, password=None):
        
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        
        user = self.create_user(email,password=password)
        user.username = username
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, verbose_name="email")
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    profile = models.ImageField(upload_to="images/", default=None)
    
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    # user_type = models.OneToOneField(UserType, on_delete=models.CASCADE)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    
     


