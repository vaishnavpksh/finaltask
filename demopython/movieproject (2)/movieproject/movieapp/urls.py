
from django.urls import path
from   . import views
app_name='movieapp'

urlpatterns = [

    path('', views.demo, name='demo'),
    path('Homepage',views.Homepage,name="Homepage"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('categories', views.categories, name='categories'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('animewatching', views.animewatching, name='animewatching'),
    path('blog', views.blog, name='blog'),





]