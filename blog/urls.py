from unicodedata import name
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('' , views.blog_list , name ="blog_list"),
    path('<int:id>' , views.blog_detail , name='blog_detail'),
    path('tag/<slug:tag>' , views.tag_blog , name='tag_blog'),
    path('category/<slug:category>',views.category_blog,name='category_blog'),
    path('search/' , views.search , name='search')
]
