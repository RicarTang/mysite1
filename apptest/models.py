from django.db import models

# Create your models here.
class UserInfo(models.Model):  # 继承这个类，固定写法
    user = models.CharField(max_length=20)  # 创建字段，最大长度为20，类型为char
    pwd = models.CharField(max_length=20)