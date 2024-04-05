from django.shortcuts import render,redirect
from django.views.generic import DetailView
from car.models import Car_Model,Order
from car.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView


class CarDetailsView(DetailView):
    model = Car_Model
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
        car_model_objects = Car_Model.objects.all()
        print(car_model_objects)
        return super().get(request, *args, **kwargs,)
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_model = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_model = car_model
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_model = self.get_object()
        comments = car_model.comments.all()
        data = Car_Model.objects.all()
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['car'] = car_model
        context['data'] = data
        return context

class CarDetailsView2(LoginRequiredMixin, DetailView):
    model = Car_Model
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        car_model_objects = Car_Model.objects.all()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_model = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_model = car_model
            new_comment.save()
        if request.user.is_authenticated:
            # Logic to create an order for the authenticated user
            # Reduce the quantity of the car model by one
            order = Order(user=request.user, car_model=car_model)
            order.save()
            car_model.quantity -= 1
            car_model.save()
            messages.success(request, 'Car purchased successfully!')
        else:
            messages.error(request, 'You need to be logged in to buy this car.')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_model = self.get_object()
        comments = car_model.comments.all()
        data = Car_Model.objects.all()
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['car'] = car_model
        context['data'] = data
        return context
    
    
def purchase_car(request, id):
    if request.user.is_authenticated:
        try:
            car_model = Car_Model.objects.get(id=id)
            if car_model.quantity > 0:
                order = Order(user=request.user, car_model=car_model)
                order.save()
                car_model.quantity -= 1
                car_model.save()
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.error(request, 'This car is out of stock.')
        except Car_Model.DoesNotExist:
            messages.error(request, 'Car not found.')
    else:
        messages.error(request, 'You need to be logged in to buy this car.')
    return redirect('car_details', id=id)


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)