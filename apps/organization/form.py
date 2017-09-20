# -*- coding: UTF-8 -*-
from django import  forms
import re
from operation.models import  UserAsk
from operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','phone','course_name']



    def clean_phone(self):
        phone = self.cleaned_data['phone']

        reg_mobile = '^1[358]\d{9}$'
        p = re.compile(reg_mobile)
        if p.match(phone):
            return phone
        else:
            raise  forms.ValidationError(u'手机号码非法',code='mobile_invalid')








