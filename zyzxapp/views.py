#encoding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from models import UserInfo, Project, WeeklyPaper
from forms import UserForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def login(request):
    if request.method == 'post':
        userid = request.POST.get('userid', '')
        password = request.POST.get('password', '')
        userobj = UserInfo.objects.get(userid=userid, password=password)

        if userobj:
            render(request, 'index.html', {'username': userid})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userid = userform.cleaned_data['userid']
            username = userform.cleaned_data['username']
            password1 = userform.cleaned_data['password1']
            password2 = userform.cleaned_data['password2']
            if password1 != password2:
                render(request, 'register.html', {'userform': userform, 'is_err': True, 'err_message': '再次输入的密码不一致'})
            email = userform.cleaned_data['email']
            phone = userform.cleaned_data['phone']

            UserInfo.objects.create(userid=userid, username=username, password=password1, email=email, phone=phone)
            # obj_userinfo = UserInfo(userid=userid, username=username, password=password1, email=email, phone=phone)
            # obj_userinfo.save()

            return redirect(to='index')
    else:
        userform = UserForm()
    return render(request, 'register.html', {'userform': userform, 'is_err': True, 'err_message': '注册成功'})


def register2(request):
    if request.method == 'POST':
        userid = request.POST.get('userid', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 != password2:
            return render_to_response('register2.html', RequestContext(request, {'is_err':True, 'err_message':'两次输入的密码不一致'}))
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        User.objects.create_user(userid=userid, username=username, password=password1, email=email, phone=phone)
        User.save()
        return render_to_response('register2.html', RequestContext(request, {'is_err': True, 'err_message' : '注册成功'}))
    else:
        return render_to_response('register2.html', RequestContext(request, {'is_err': False, 'err_message': '两次输入的密码不一致'}))



def proj_progress(request):
    context = {}
    proj_list = Project.objects.all()
    context['proj_list'] = proj_list
    weekly_paper_page = render(request, 'proj_progress.html', context)
    return weekly_paper_page


def weekly_paper(request):
    context = {}
    weekly_paper_list = WeeklyPaper.objects.all()
    context['weekly_paper_list'] = weekly_paper_list
    weekly_paper_page = render(request, 'weekly_paper.html', context)
    return weekly_paper_page





