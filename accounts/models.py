from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class usersmanager(BaseUserManager):
        def create_user(self,first_name,last_name,email,password = None):
            if not email:
                raise ValueError("User must provide an email address")
            if not first_name or not last_name:
                raise ValueError("User must provide their first and last name")
            
            user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
        
        def create_superuser(self,first_name,last_name,email,password=None):
            user = self.create_user(email =email,
                password= password,
                first_name = first_name,
                last_name=last_name,
                )
            user.is_admin = True
            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)
            return user





class users(AbstractBaseUser):
    first_name = models.CharField(max_length=40,null=False)
    last_name = models.CharField(max_length=40,null=False)
    email = models.EmailField(max_length=200,unique=True,null=False,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =   ['first_name','last_name']

    objects = usersmanager()

    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self)-> str:
        return f"{self.first_name} {self.last_name}"

