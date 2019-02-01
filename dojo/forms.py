#dojo/forms.py

from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class PostForm(forms.Form):
    title = forms.CharField(validator=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
    #위젯옵션을 통해 여러 줄을 입력받도록 함.

