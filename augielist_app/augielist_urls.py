from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_list, name='category_list'),
    path('new', views.new_category, name='new_category'),
    path('<int:category_id>', views.category_detail, name='category_detail'),
    path('<int:category_id>/edit', views.edit_category, name='edit_category'),
    path('<int:category_id>/delete', views.delete_category, name='delete_category'),
    path('<int:category_id>/posts', views.posts_list, name='posts_list'),
    path('<int:category_id>/posts/new', views.new_post, name='new_post'),
    path('<int:category_id>/posts/<int:post_id>', views.post_detail, name='post_detail'),
    path('<int:category_id>/posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:category_id>/posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
]