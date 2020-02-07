from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from index.models import Post
# Create your models here.
class PicTest(models.Model):
    #相对于媒体目录的路径
    goods_pic = models.ImageField(upload_to='pic/')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)