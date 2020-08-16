from django.shortcuts import render,redirect
from .models import BlogModel
from .forms import BlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    blogs = BlogModel.objects.order_by('-created')
    context = {'blogs' : blogs}
    return render(request, 'index.html', context)

def details(request,blog_id):
    blogs = BlogModel.objects.get(id=blog_id)
    context = {'blogs': blogs}
    return render(request, 'blog_details.html', context)

def create_blog_post(request):
    if request.method == 'GET':
        context = {'form': BlogForm()}
        return render(request, 'create_blog_post.html', context)
    else:
        try:
            if request.POST['title'] == '':
                context = {'form': BlogForm(), 'error': 'Please enter title.'}
                return render(request, 'create_blog_post.html', context)
            elif request.POST['description'] == '':
                context = {'form': BlogForm(), 'error': 'Please enter description.'}
                return render(request, 'create_blog_post.html', context)
            elif request.POST['user'] == '':
                context = {'form': BlogForm(), 'error': 'Please enter user.'}
                return render(request, 'create_blog_post.html', context)
            else:
                form = BlogForm(request.POST)
                form.save()
                return redirect('home')
            
        except ValueError:
            context = {'form': BlogForm(), 'error': 'Bad request. Try again.'}
            return render(request, 'create_blog_post.html', context)

def edit_details(request,blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    print(blog.title+","+blog.description)
    if request.method == 'GET':
        bform = BlogForm(instance=blog)
        context = {'blog': blog, 'bform': bform}
        return render(request, 'edit_details.html', context)
    else:
        try:
            blogform = BlogForm(request.POST,instance=blog)
            if blogform.is_valid():
                blogform.save()
                return redirect('home')
            else:
                return render(request,"edit_details.html", {"bform": blogform})
        except ValueError as ve:
            context = {'blog': blog, 'bform': blogform, 'error': ve}
            return render(request, 'edit_details.html', context)
            
    



