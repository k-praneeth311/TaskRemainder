from django.urls import path
from tasks import views

urlpatterns = [
	path('',views.home,name='home'),
    path('index/<str:fk>',views.index,name='index'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]