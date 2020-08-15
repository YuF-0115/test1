from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class Home(TemplateView):
    template_name = 'mamazon/home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'mamazon/list.html'
    #Listを作るだけなら上のだけでok, 検索キーワードとかの機能を付けたいので, 下のqueryをつける
    def get_queryset(self):
        queryset = Product.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__contains=qs)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'mamazon/detail.html'
