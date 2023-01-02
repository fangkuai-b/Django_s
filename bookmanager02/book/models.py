from django.db import models

# Create your models here.
'''
https://docs.djangoproject.com/zh-hans/2.0/
1、模型类 需要继承自 models.Model
2、定义属性
    id 系统默认会生成；
    属性名=models.类型（选项）
    2.1 属性名对应就是字段名
        不要使用Python和mysql关键字
        不要使用连续的下划线（__）
    2.2 类型 mysql的类型
    2.3 选项 是否有默认值，是否唯一，是否为null，
        CharField 必须设置max_length
        verbose_name 主要是admin站点使用
3、改变表的名称
    默认表的名称：子应用名_类名  都是小写
    修改表的名字
'''


# 准备书籍模型类
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=20, verbose_name='名称', unique=True)
    pubdate = models.DateField(verbose_name='发布日期', null=True)
    read_count = models.IntegerField(default=0, verbose_name='阅读量')
    comment_count = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除状态')

    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        return self.name


# 准备人物的模型类
class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = {
        (0, 'male'),
        (1, 'female')
    }
    # 创建字段，字段类型
    name = models.CharField(max_length=10, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name='性别')
    description = models.CharField(max_length=300, null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 外键
    # 系统会自动为外键添加 _id
    # 外键的级联操作
    # 主表和从表
    # 一 对 多（书籍 对 人物）
    # CASCADE级联，删除主表数据时连通一起删除外键表中数据
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')

    class Meta:
        db_table = 'peopleinfo'  # 指明数据库表名
        verbose_name = '人物信息'  # 在admin站点中显示的名称

    def __str__(self):
        return self.name
