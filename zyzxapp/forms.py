#encoding:utf-8
from django import forms


class UserForm(forms.Form):
    userid = forms.CharField(
        max_length=8,
        min_length=8,
        required=True,
        label=u'用户名',
        error_messages={'required': u'请输入登录名'},
        widget=forms.TextInput(attrs={'placeholder': u"用户登录名", }),

    )
    username = forms.CharField(
        required=True,
        label=u"姓名",
        error_messages={'required': u'请输入真实姓名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"姓名",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"密码",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请再次输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"请再次输入密码",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        label=u"电子邮箱",
        error_messages={'required': u'请输入正确的电子邮箱'},
        widget=forms.EmailInput(
            attrs={
                'placeholder': u"请输入正确的电子邮箱",
            }
        ),
    )
    phone = forms.CharField(
        required=True,
        label=u"联系方式",
        error_messages={'required': u'请输入手号码'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"请输入手机号码",
            }
        ),
    )
