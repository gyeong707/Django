from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
import os

class PostListView1(View):
    def get(self, request):
        name = "경"
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)


    def get_template_string(self):
        return '''
        <h1> AskDjango </h1>
        <p> {name} </p>
        <p> 여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
        '''
        
post_list1 = PostListView1.as_view()
#이런식으로 구조적으로 개발이 가능하다.
#앞에서의 그냥 post_list1과 이 함수는 완벽히 같다!
#상황에 따라 어느 것으로 개발할 지 정해서 하자.



class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = "경"
        return context

post_list2 = PostListView2.as_view()



class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
            'message' : '안녕, 파이썬&장고',
            'items' : ['파이썬', '장고', 'Celery', 'Azure', "AWS"],
          }

post_list3 = PostListView3.as_view()
#뷰를 상속받아 쓴 이유? 
#함수기반으로 작성된 코드를 클래스기반으로도 할 수 있다는 것을 보여주기 위함.


class ExcelDownloadView(View):
    
    excel_path = 'C:/django/askdjango/test.xlsx'

    def get(self, request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
                response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
                # 필요한 응답헤더 세팅
                response['Content-Disposition'] = 'attachment; filename="{}"' .format(filename)
                return response

