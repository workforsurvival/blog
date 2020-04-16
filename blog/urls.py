from django.urls import path
# from .views import home_page, category_page, post_page, contact_page
from .views import (
    ContactCreateView,
    ContactListView,
    # COntactDetailView,
)
app_name = 'blog'
urlpatterns = [
    path('', ContactListView.as_view(), name='home-page'),
    path('home/', ContactListView.as_view(), name='home-page'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
]
