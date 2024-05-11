from django.urls import path
from . import views



urlpatterns = [
    path('home/' , views.home , name="blogs"),
    path('<slug:slug>', views.blog_page, name="page"),
    path('add-blog/', views.blog_new, name="add-blog"),
]