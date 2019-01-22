from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os

# Create your views here.
def mysum(request, numbers):
    #request: HttpRequest
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요' .format (name, age))

#http 리스폰스#
def post_list1(request):
    name = "강미경"
    return HttpResponse('''
    <h1> AskDjango </h1>
    <p> {name} </p>
    <p> 여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


#템플릿 응답#
def post_list2(request):
    name = "미경"
    return render(request , 'dojo/post_list.html', {'name':name})


#제이슨 응답#
def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬&장고', 'items' : ['파이썬', '장고', 'Celery', 'Azure'],
    }, json_dumps_params={'ensure_ascii': False})


#파일 다운로드 응답#
def excel_download(request):
    filepath = 'C:/django/askdjango/test.xlsx'
    filename = os.path.basename(filepath)
    #파일 이름부분만 추출
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        #기본이 text/html임. 근데 우리는 excel 형식이니까 application~으로 지정해주어야 하는 것.
        response['Content-Disposition'] = 'attachment; filename="{}"' .format(filename)
        return response
