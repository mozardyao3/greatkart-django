from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    #Create a normal user in this function#
    def create_user(self,  first_name, last_name, username, email,  registration_number, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            registration_number = registration_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #Create a superuser in this function#
    def create_superuser(self, first_name='Yao', last_name='mozard', email='mozardyao@gmail.com', username='yao',  registration_number='56567646977/', password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
            registration_number = registration_number,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin  = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'registration_number']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self,perm, obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True