from django.db import models
from accounts.models import users

import string
import random

# main classroom model
class room(models.Model):
    creater = models.ForeignKey(users,on_delete=models.RESTRICT)
    code = models.CharField(max_length=8,null=False,unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

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
        return f"creater = {self.creater_id}, {self.name=}"

# to store the messages (and later files) in classroom
class content(models.Model):
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    msg = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.msg

# join table to keep track of students who join a class
class member(models.Model):
    student = models.ForeignKey(users,on_delete=models.CASCADE)
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student','room',)

    def __str__(self) -> str:
        return f"user {self.user_id} joined class {self.class_id} on {self.date_joined}"

    def is_member(self,user_pk):
        if self.objects.filter(student_id = user_pk).exists() :
            return True
        return False
