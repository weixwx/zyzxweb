#encoding:utf-8
from django.contrib import admin
from models import UserInfo, Project, WeeklyPaper


admin.site.register(UserInfo)
admin.site.register(Project)
admin.site.register(WeeklyPaper)


