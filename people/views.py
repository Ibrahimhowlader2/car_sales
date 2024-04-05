from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import userSignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from car.models import Car_Model
from car.models import Order
# Create your views here..

class signUpView(View):
    template_name = 'signUp.html'
    form_class = userSignUpForm
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logIn')
        return render(request, self.template_name, {'form': form})

class logInView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)


class logOutView(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
@method_decorator(login_required,name='dispatch')
class editProfileView(UpdateView):
    model = User
    fields = ['username','first_name', 'last_name', 'email']
    template_name = 'edit_profile.html'
    
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')



@method_decorator(login_required,name='dispatch')
class profileView(View):
    def get(self, request):
        orders=Order.objects.filter(user=request.user)
        return render(request, 'profile.html',{"orders":orders})
   
        
def buyCar(request,id):
    car=Car_Model.objects.get(id=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        order=Order.objects.create(user=request.user,car_model=car)
        order.save()
        return render(request, 'profile.html',)
    else:
        return render(request, 'car_details.html')

@method_decorator(login_required,name='dispatch')
class changePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('logIn')
