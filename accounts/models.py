from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser # django app 은 user 모델이 필수로 가져야할 필요 스펙들이 있음


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성" # db 저장될값, 보여질 값
        FEMALE = "F", "여성"

    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")



