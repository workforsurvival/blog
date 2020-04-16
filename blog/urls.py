from django.urls import path
from .views import home_page, category_page, post_page

app_name = 'blog'
urlpatterns = [
    path('', home_page, name='home-page'),
    path('home/', home_page, name='home-page'),
    path('category/', category_page, name='category-page'),
    path('post/', post_page, name='post-page'),
]
