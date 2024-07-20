from typing import Any
from django.views.generic import View
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello Hitman #45❤️ </h1>")


class TemplateCBV(TemplateView):
    template_name='testapp/result.html'


class TemplateCBV2(TemplateView):
    template_name='testapp/result2.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name']='Durga'
        context['makrs']=100
        context['subject']='Django'
        return context
