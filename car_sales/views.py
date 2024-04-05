from django.shortcuts import redirect,render
from django.views import View
from car.models import Car_Model
from brand.models import BrandModel



def home(request, category_slug=None):
    data = Car_Model.objects.all()
    if category_slug is not None:
        category=BrandModel.objects.get(slug=category_slug)
        data=Car_Model.objects.filter(brand=category)
    categories=BrandModel.objects.all()
    return render(request,'home.html',{'data':data,'category':categories})

class brandCategoryView(View):
    template_name='home.html'
    def get(self,request,slug):
        brand=BrandModel.objects.get(slug=slug)
        cars=Car_Model.objects.filter(brand=brand)
        all_cars=Car_Model.objects.all()
        context={'cars':cars, 'all_cars':all_cars, 'brand':brand}
        return render(request,self.template_name,context)