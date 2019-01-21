from django.shortcuts import render

#blog/views.py

def post_list(request):
    return render(request, 'blog/post_list.html')

