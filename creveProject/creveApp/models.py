from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class CustomUserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# ==================== CUSTOM USER MODEL ============================
class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(
        max_length=255, unique=True, blank=True, null=True)

    profilePic = models.ImageField(
        upload_to='profile_pics/', default='default.png', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_creative = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def _str_(self):
        return self.email


# ======================== CREATIVE PROFILE ==========================
class CreativeAccount(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    phoneNumber = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=255, blank=True, null=True)

    validDocument = models.ImageField(
        upload_to='profile_pics/', default='default.png', blank=True, null=True)
    ninDocument = models.CharField(max_length=255, blank=True, null=True)

    accountName = models.CharField(max_length=255, blank=True, null=True)
    accountNumber = models.CharField(max_length=255, blank=True, null=True)
    bankName = models.CharField(max_length=255, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.account.name
    # except:
    #     def __str__(self):
    #         return self.account.name


# ======================== USER ACCOUNT =========================
class UserAccount(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', default='default.png', blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.account.name


# ========================= CATEGORYS =================================
class Category(models.Model):
    categoryName = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.categoryName



 # ========================= PRODUCTS =================================


class Product(models.Model):

    creator = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    images = ArrayField(models.ImageField(upload_to='products/'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
