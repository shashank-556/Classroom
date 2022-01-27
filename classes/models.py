from django.db import models
from accounts.models import users

import string
import random

# main classroom model
class room(models.Model):
    creater = models.ForeignKey(users,on_delete=models.RESTRICT,related_name='created_classes')
    code = models.CharField(max_length=8,null=False,unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField(users,related_name='rooms')

    # random string of lowercase a-z of len 6 to 8 for class code
    @staticmethod
    def generate_code():
        
        while True:
            length = random.randint(6,8)
            code = ''.join(random.choices(string.ascii_lowercase,k=length))
            if room.objects.filter(code = code).count() == 0:
                break
        return code

    def __str__(self) -> str:
        return f"creater = {self.creater.id}, {self.name=}"

# to store the messages (and later files) in classroom
class content(models.Model):
    room = models.ForeignKey(room,on_delete=models.CASCADE,related_name='contents')
    msg = models.CharField(max_length=200, null=False)
    sheet = models.FileField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.msg

