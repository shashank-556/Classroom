from django.db import models
from accounts.models import users

class info(models.Model):
    creater_id = models.ForeignKey(users,on_delete=models.RESTRICT)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class content(models.Model):
    class_id = models.ForeignKey(info,on_delete=models.CASCADE)
    msg = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-class_id','-created_at']

class member(models.Model):
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)
    class_id = models.ForeignKey(info,on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

