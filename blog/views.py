from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #this classes work with paginator
from django.views.generic import ListView # class view
from .models import Post

# Create your views here.

# list all posts
#def post_list(request):
#    posts = Post.published.all()
#    return render(request,'blog/post/list.html',{'posts':posts})

# list all post further add paginator 
#def post_list(request):
#    object_list = Post.published.all()
#    paginator = Paginator(object_list, 3) # 3 posts in each page
#    page = request.GET.get('page') # indicate the current page
#
#    try:
#        posts = paginator.page(page) 
#        #obtain the objects for the desired page by calling the page() method of paginator
#    except PageNotAnInteger:
#        # If page is not an integer deliver the first page
#        posts = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range deliver last page of results
#        posts = paginator.page(paginator.num_pages)

#    return render(request,
#                    'blog/post/list.html',
#                    {'page': page,
#                    'posts': posts})

# list post with class based views
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'



#post detail
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,
                                )

    return render(request, 'blog/post/detail.html',{'post':post})

