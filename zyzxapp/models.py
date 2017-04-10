#encoding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import date


class UserInfo(models.Model):
    userid = models.CharField(null=False, blank=False, max_length=8, primary_key=True)
    username = models.CharField(null=False, blank=False, max_length=32)
    password = models.CharField(null=False, blank=False, max_length=128)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return self.userid


class Project(models.Model):
    projid = models.CharField(null=False, blank=False, max_length=8, primary_key=True)
    projname = models.CharField(null=False, blank=False, max_length=128)
    begtim = models.DateField(null=False, blank=False, default=date.today)
    endtim = models.DateField(null=False, blank=False, default=date.today)
    sttim = models.DateField(null=False, blank=False, default=date.today)
    uattim = models.DateField(null=False, blank=False, default=date.today)
    realendtim = models.DateField(null=False, blank=False, default=date.today)
    userid = models.CharField(null=False, blank=False, max_length=8)
    projmember = models.CharField(null=False, blank=False, max_length=128)
    projstatus = models.CharField(null=False, blank=False, max_length=2)

    def __str__(self):
        return self.projid


class WeeklyPaper(models.Model):
    userid = models.ForeignKey('UserInfo')
    update_time = models.DateTimeField(null=False, blank=False, default=timezone.now, editable=False)
    work_desc = models.TextField(null=False, blank=False, max_length=1024)
