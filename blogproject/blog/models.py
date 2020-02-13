from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '标签 '
        verbose_name_plural = verbose_name

# 文章
class Post(models.Model):

    # 标题
    title = models.CharField('标题',max_length=70)

    # 文章正文
    body = models.TextField('正文')

    # 创建时间
    create_time = models.DateTimeField('创建时间',default=timezone.now)
    # 修改时间
    modified_time = models.DateTimeField('修改时间')
    # 文章摘要
    excerpt = models.CharField('摘要',max_length=200,blank=True)
    # 分类 一对多的外键
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    # 标签 多对多
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)

    # 文章作者 User从django.contrib.auth.models导入
    author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)

    #自定义app页面
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    # 人性化的返回值
    def __str__(self):
        return self.title

    #每一个model都有一个save方法，通过覆盖这个方法可以在model被save到数据库前指定modified_time的值为当前时间
    def save(self,*args,**kwargs):
        self.modified_time = timezone.now()
        super().save(*args,**kwargs)

    # 自定义 get_absolute_url 方法
    # 从django.urls中导入reverse方法
    # 反解析url
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
