from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo


# Create your views here.
def index(request):
    # 在这里实现 增删改查
    return HttpResponse("index")


##############################增加##################################
# 增加
# 方式一
book = BookInfo(
    name='python入门',
    pubdate='2023-01-04',
    read_count='123'
)
book.save()

# 方式二
BookInfo.objects.create(
    name='Django入门',
    pubdate='2012-01-23'
)

##############################修改##################################
# 修改
# 方式一
book = BookInfo.objects.get(id=5)
book.name = '运维开发入门'
book.save()

# 方式二
# filter 过滤
BookInfo.objects.filter(id=6).update(name='python 入门必备', comment_count='111')

##############################删除##################################
# 删除
# 方式一
# 物理删除
book = BookInfo.objects.get(id='6')
book.delete()
# 逻辑删除，即修改is_delete=False删除标记，同update

# 方式二
BookInfo.objects.get(id=7).delete()
BookInfo.objects.filter(id=5).delete()

##############################查询##################################
# 查询
# get   查询单一结果
book = BookInfo.objects.get(id=1)  # <BookInfo: 射雕英雄传>

# all   查询多个结果
books = BookInfo.objects.all()  # <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>]>

# get 查询单一结果，不存在则 raise self.model.DoesNotExist
try:
    book = BookInfo.objects.get(id=120)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# count 查询结果数量
BookInfo.objects.count()
BookInfo.objects.all().count()

##############################过滤查询##############################
'''
实现SQL中的where功能，包括
    filter过滤出多个结果
    exclude排除掉符合条件剩下的结果
    get过滤单一结果
对于过滤条件的使用，上述三个方法相同，故仅以filter进行讲解。
过滤条件的表达语法如下：属性名称__比较运算符=值
    属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线
'''

# 查询编号为1的图书
BookInfo.objects.get(id__exact=1)  # <BookInfo: 射雕英雄传>     get 得到的是一个
BookInfo.objects.filter(id__exact=1)  # <QuerySet [<BookInfo: 射雕英雄传>]>    filter 得到的是列表
BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=1)  # pk 为primary key   主键

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 2, 5))

# 查询编号大于3的图书
# gt大于 (greater then)
# gte大于等于 (greater then equal)
# lt小于 (less then)
# lte小于等于 (less then equal)
BookInfo.objects.filter(id__gt='3')

# 查询编号不等于3的图书
BookInfo.objects.exclude(id__exact='3')

# 查询1980年发表的图书
BookInfo.objects.filter(pubdate__year='1980')

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pubdate__gt='1990-01-01')
