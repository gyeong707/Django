
import re
from django.forms import ValidationError
from django.utils import timezone
from django.db import models

# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name = "제목", 
    help_text = "포스팅 제목을 입력해주세요."
        # choices = (
        #     ('제목1', '제목1 레이블'),
        #     ('제목2', '제목2 레이블'), #('저장될 값', 'UI에 보여질 레이블')
    
        # )
    )
    content = models.TextField(verbose_name = "내용", help_text="내용을 입력해주세요")            # 길이 제한이 없는 문자열 : Textfield 
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='경도, 위도 포맷으로 입력',
    validators = [lnglat_validator],) #함수 자체를 인자로 넘김,
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    