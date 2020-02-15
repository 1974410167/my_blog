from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect
import markdown
from .models import Category,Tag,Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q

def index(request):
    post_list=Post.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    # 如果不存在自动报404错误
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request,'blog/detail.html',context={'post':post})

def archive(request, year, month):

    post_list = Post.objects.filter(create_time__year=year,

                                    create_time__month=month

                                    ).order_by('-create_time')

    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):

    # 记得在开始部分导入 Category 类

    cate = get_object_or_404(Category, pk=pk)

    post_list = Post.objects.filter(category=cate).order_by('-create_time')

    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def idea(request):
    return render(request,'blog/idea.html')

# 分页




def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})
