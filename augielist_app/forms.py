from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'post_title', 'post_price', 'post_description', 'post_email')

