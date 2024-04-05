from django.urls import path
from . import views
urlpatterns=[
   path("car_details/<int:id>", views.CarDetailsView.as_view(),name="car_details"),
   path("purchase/<int:id>", views.purchase_car, name="purchase_car"),
   path("order_history/", views.OrderHistoryView.as_view(), name="order_history"),
   
]