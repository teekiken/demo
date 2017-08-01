# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#一个class代表一个数据表
#一个类属性代表一个字段
class MyappModels(models.Model):   #定义应用模型映射到数据库里，类名为app名称+Models，类名首字母大写
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=False)
    content = models.TextField(null=False)
    link = models.CharField(max_length=100,null=False)
