from django.shortcuts import render
from django.shortcuts import HttpResponse  # 3,导入响应模块
from apptest import models  # 导入models模块


# Create your views here.
# user_list = []  # 8，增加一个空列表

def index(request):  # 4,第一个参数必须是request，名字可以改，但最好不要改，这是潜规则。request参数封装了用户请求的所有内容
    # return HttpResponse('Hello world!')  # 5,不能直接返回字符串，要用这个类封装起来才能被HTTP协议识别
    if request.method == 'POST':  # 7，判断前端发送的请求方式，是post执行下面代码
        username = request.POST.get('username')  # 得到前端提交的内容
        password = request.POST.get('password')
        # temp = {"user":username,"pwd":password}  # 9，拿到的前端数据放进字典
        # user_list.append(temp)  # 字典放进数组
        # print(username,password)
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    # 10,将用户列表作为上下文参数供render渲染到index页面
    # 从数据库读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request,'index.html',{"data":user_list})  # 6,render方法使用数据字典和请求元数据，渲染一个指定的HTML模板。多个参数中，第一个参数必须是request，第二个是模板
