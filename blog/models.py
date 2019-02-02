
import re
from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    objects = models.Manager()

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    # author = models.CharField(max_length=100)
    title = models.CharField(max_length=100, verbose_name = "제목", 
    help_text = "포스팅 제목을 입력해주세요."
        # choices = (
        #     ('제목1', '제목1 레이블'),
        #     ('제목2', '제목2 레이블'), #('저장될 값', 'UI에 보여질 레이블')
    
        # )
    )
    content = models.TextField(verbose_name = "내용", help_text="내용을 입력해주세요")            # 길이 제한이 없는 문자열 : Textfield
    photo = models.ImageField(blank=True)
    
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='경도, 위도 포맷으로 입력',
    validators = [lnglat_validator],) #함수 자체를 인자로 넘김,

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name