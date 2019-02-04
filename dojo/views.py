from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import os
from .forms import PostForm
from .models import Post


def generate_view_fn(model):

    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
        return render(request, template_name, {
        instance_name: instance,
        })

    return view_fn


post_detail = generate_view_fn(Post)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            print(form.cleaned_data)
            return redirect('/dojo/') #url reverse를 쓰는 경우 해당 이름의 네임스페이스를 써야 함.
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') #url reverse를 쓰는 경우 해당 이름의 네임스페이스를 써야 함.
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })



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



####post_new에서 객체 저장하는 방법 -- 최종적으로는 방법(4)를 사용함 ####
 # 방법(1)
    # post = Post()
    # post.title = form.cleaned_data['title']
    # post.content = form.cleaned_data['content']
    # post.save()

# 방법(2)
    # post = Post(title=form.cleaned_data['title'],
    #             content = form.cleaned_data['content'])
    # post.save()

 # 방법(3)
    # post = Post.objects.create(title=form.cleaned_data['title'],
    #                             content=form.cleaned_data['content'])

