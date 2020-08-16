from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:blog_id>/',views.details,name='details'),
    path('createBlogPost/', views.create_blog_post, name='create'),
    path('edit_details/<int:blog_id>/', views.edit_details, name='edit'),
]
