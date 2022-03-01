from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from blog.models import Blog, Comment

# Create your views here.
def home_view(request):
    return render(request, 'blog/landing.html', {})

def blog_view(request):
    post_list = Blog.objects.order_by('-id')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    contest = {
        'post': post
    }
    return render(request, 'blog/blog.html', contest)

def blog_form_view(request):
    if request.method == 'POST':
        post=Blog()
        post.title = request.POST.get('title')
        post.desc1 = request.POST.get('desc1')
        post.desc2 = request.POST.get('desc2')
        if len(request.FILES) != 0:
            post.image1 = request.FILES['image1']
        post.brief = request.POST.get('brief')
        post.desc3 = request.POST.get('desc3')
        post.summary = request.POST.get('summary')
        if len(request.FILES) != 0:
            post.image2 = request.FILES['image2']
        post.save()
        messages.success(request, "Post has been uploaded")
    else:
        post = Blog()
    return render(request, 'blog/blog_form.html')

def blog_details_view(request, blog_slug):
    if request.method == 'POST':
        instance = get_object_or_404(Blog, blog_slug=blog_slug)
        comment = Comment()
        comment.user_name = request.POST.get('name')
        comment.email_address = request.POST.get('email')
        comment.message = request.POST.get('message')
        comment.blog = instance
        comment.save()
        messages.success(request, "Comment dropped successfully")

    all_comments = Comment.objects.all().order_by('-date_created')
    blog_details = Blog.objects.get(blog_slug=blog_slug)
    contest = {
        'blog': blog_details,
        'comment': all_comments,}
    return render(request, 'blog/blog_single.html', contest)

