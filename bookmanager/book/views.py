from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
视图
所谓的视图，其实就是Python函数
视图函数有两个要求：
    1.视图函数的第一个参数就是接收请求.这个请求其实就是 HTTPRequest的类对象
    2.必须返回一个响应
'''


# 还需要定义路由即我们期望用户输入 http://127.0.0.1:8000/index 来访问我们的视图函数
def index(request):
    # return HttpResponse('OK')
    # request, template_name, context = None, content_type = None, status = None, using = None
    # request   请求
    # template_name 模板名
    # context = None
    return render(request, 'book/index.html')
