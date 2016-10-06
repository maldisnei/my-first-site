from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment

def index(request):
    postes = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request,'blog/index.html',{'postes':postes})


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/detail.html',{'post':post})
@login_required   
def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.auth = request.user
            
            post=form.save()
            return redirect('blog.views.detail', pk=post.pk )
    else:
        form = PostForm()

    return render(request,'blog/post_draft.html',{'form':form})
@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth=request.user
            
            post=form.save()
            return redirect('blog.views.detail', pk=post.pk)
    else:
        form=PostForm(instance=post)

    return render(request,'blog/post_draft.html',{'form':form})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blog/post_draft_list.html',{'posts':posts})
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('detail',pk=pk)
@login_required
def post_remove(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('index')

def add_comment_to_post(request,pk):
    post= get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/add_comment_to_post.html',{'form':form})
@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approved()
    return redirect('detail', pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('detail',pk=post_pk)
