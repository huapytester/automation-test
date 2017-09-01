# coding:utf-8
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View


# 欢迎页
def welcome_page(request):
    return render(request, 'hello.html')


# 自定义登录类
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print request.POST
        if request.POST.get('username', '') == 'lizhenghua' and request.POST.get('passwd', '') == '1111':
            request.session['user'] = request.POST.get('username', '')
            return redirect('/user_action/')
        else:
            return render(request, 'login.html', {'erro': 'username or passwd erro'})


# 个人中心
def user_action(request):
    username = request.session.get('user', '')
    if username:
        return render(request, 'login_action.html', {'username': username})
    else:
        return redirect('/')


# # 登录页面
# def login(request):
#     if request.method == 'POST':
#         if request.POST.get('username', '') == 'lizhenghua' and request.POST.get('passwd', '') == '1111':
#             return render(request, 'html/login_action.html')
#         else:
#             return render(request, 'html/login.html', {'erro': 'username or passwd erro'})
#     return render(request, 'html/login.html')
