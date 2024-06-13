from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
)
from .models import User

class SignupForm(UserCreationForm):
    # 생성자
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필수 필드로 설정
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    class Meta(UserCreationForm.Meta): # 기본 기능은 유지한채 필드정보만 추가
        model=User # 우리가 커스텀한 모델
        fields = ['username', 'email', 'first_name', 'last_name']
    def clean_email(self):
        email = self.cleaned_data.get('email') # orm 안에서 validate된 후에, 즉 검증된 후의 적당한 데이터가 들어 있는 변수
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소 입니다.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'website_url',
                  'bio', 'phone_number', 'gender']


class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password and new_password1:
            if old_password == new_password1:
                raise forms.ValidationError("새로운 암호는 기존 암호과 다르게 입력해주세요.")
        return new_password1