from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Post
from .forms import CategoryForm, PostForm

def get_category(category_id):
    return Category.objects.get(id=category_id)

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_category(category_id)
    return render(request, 'categories/category_detail.html', {'category': category})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request': 'New'})

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, category_id):
    if request.method == "POST":
        category = get_category(category_id)
        category.delete()
    return redirect('category_list')

def get_post(post_id):
    return Post.objects.get(id=post_id)

def posts_list(request, category_id):
    category = get_category(category_id)
    posts = category.posts.all()
    return render(request, 'categories/posts_list.html', {'category': category, 'posts': posts})

def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    return render(request, 'categories/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'categories/post_form.html', {'form': form, 'type_of_request': 'New'})

def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'categories/post_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_post(request, category_id, post_id):
    if request.method == "POST":
        post = get_post(post_id)
        post.delete()
    return redirect('posts_list', category_id=category_id)