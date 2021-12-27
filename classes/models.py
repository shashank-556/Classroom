from django.db import models

class info(models.Model):
    # creater_id
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class content(models.Model):
    classid = models.ForeignKey(info,on_delete=models.CASCADE)
    msg = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-classid','-created_at']

